# Shure SRH840
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.5; 34 -2.6; 37 -3.5; 41 -4.7; 45 -5.6; 49 -6.4; 54 -7.4; 60 -8.2; 66 -8.7; 72 -9.0; 79 -9.1; 87 -9.3; 96 -9.6; 106 -10.0; 116 -10.1; 128 -10.5; 141 -10.7; 155 -10.5; 170 -9.5; 187 -10.1; 206 -10.0; 227 -9.7; 249 -9.5; 274 -9.3; 302 -10.9; 332 -10.5; 365 -9.9; 402 -9.5; 442 -9.0; 486 -8.8; 535 -8.4; 588 -7.7; 647 -7.3; 712 -7.1; 783 -6.7; 861 -6.7; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.3; 1387 -8.0; 1526 -9.1; 1678 -9.8; 1846 -10.5; 2031 -11.0; 2234 -11.7; 2457 -11.3; 2703 -10.3; 2973 -9.5; 3270 -8.7; 3597 -7.8; 3957 -6.8; 4353 -6.8; 4788 -7.8; 5267 -5.0; 5793 -1.0; 6373 -1.0; 7010 -4.0; 7711 -6.4; 8482 -11.8; 9330 -13.4; 10263 -8.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH840 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 25 Hz    |  0.96 | 7.4 dB  |
| Peaking | 134 Hz   |  0.34 | -4.2 dB |
| Peaking | 2282 Hz  |  1.67 | -5.3 dB |
| Peaking | 6214 Hz  |  3.82 | 7.2 dB  |
| Peaking | 9064 Hz  |  4.42 | -8.3 dB |
| Peaking | 337 Hz   |  4.09 | -1.5 dB |
| Peaking | 956 Hz   |  1.54 | 1.2 dB  |
| Peaking | 1621 Hz  |  4    | -1.0 dB |
| Peaking | 4774 Hz  | 11.3  | -2.0 dB |
| Peaking | 11116 Hz |  7.15 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH840/Shure%20SRH840.png)