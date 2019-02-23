# Shure SRH840
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.6; 41 -2.8; 45 -3.7; 49 -4.4; 54 -5.4; 60 -6.3; 66 -6.8; 72 -7.0; 79 -7.1; 87 -7.3; 96 -7.7; 106 -8.0; 116 -8.2; 128 -8.6; 141 -8.7; 155 -8.5; 170 -7.5; 187 -8.1; 206 -8.0; 227 -7.7; 249 -7.5; 274 -7.3; 302 -9.0; 332 -8.6; 365 -8.0; 402 -7.5; 442 -7.0; 486 -6.8; 535 -6.4; 588 -5.7; 647 -5.3; 712 -5.1; 783 -4.8; 861 -4.7; 947 -4.3; 1042 -4.7; 1146 -4.9; 1261 -5.3; 1387 -6.0; 1526 -7.1; 1678 -7.9; 1846 -8.6; 2031 -9.1; 2234 -9.7; 2457 -9.4; 2703 -8.4; 2973 -7.5; 3270 -6.8; 3597 -5.9; 3957 -4.8; 4353 -4.9; 4788 -5.9; 5267 -3.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.9; 9330 -11.5; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.88 | 6.9 dB  |
| Peaking | 121 Hz  | 0.59 | -2.3 dB |
| Peaking | 2273 Hz | 3.16 | -3.7 dB |
| Peaking | 6036 Hz | 2.82 | 6.6 dB  |
| Peaking | 9041 Hz | 4.6  | -6.4 dB |
| Peaking | 332 Hz  | 3.8  | -1.8 dB |
| Peaking | 947 Hz  | 1.25 | 2.4 dB  |
| Peaking | 1724 Hz | 2.9  | -1.4 dB |
| Peaking | 3937 Hz | 9.66 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH840/Shure%20SRH840.png)