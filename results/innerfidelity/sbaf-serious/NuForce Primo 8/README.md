# NuForce Primo 8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.2; 25 -3.3; 28 -3.5; 31 -3.7; 34 -3.8; 37 -4.0; 41 -4.2; 45 -4.3; 49 -4.5; 54 -4.9; 60 -5.2; 66 -5.5; 72 -5.8; 79 -6.2; 87 -6.6; 96 -7.1; 106 -7.4; 116 -7.6; 128 -8.0; 141 -8.3; 155 -8.5; 170 -8.7; 187 -8.9; 206 -9.0; 227 -9.0; 249 -9.1; 274 -8.9; 302 -8.9; 332 -8.8; 365 -8.7; 402 -8.6; 442 -8.4; 486 -8.3; 535 -8.2; 588 -7.8; 647 -7.7; 712 -7.8; 783 -7.6; 861 -8.0; 947 -8.3; 1042 -8.8; 1146 -9.3; 1261 -9.9; 1387 -10.7; 1526 -11.7; 1678 -12.5; 1846 -12.8; 2031 -12.2; 2234 -10.4; 2457 -7.2; 2703 -4.1; 2973 -1.0; 3270 -0.5; 3597 -0.6; 3957 -2.2; 4353 -2.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -5.1; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce Primo 8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce Primo 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 17 Hz   |  0.28 | 3.5 dB  |
| Peaking | 208 Hz  |  0.52 | -2.8 dB |
| Peaking | 1920 Hz |  1.29 | -8.4 dB |
| Peaking | 3135 Hz |  1.84 | 8.9 dB  |
| Peaking | 5292 Hz |  3.29 | 5.8 dB  |
| Peaking | 4691 Hz | 10.79 | 1.5 dB  |
| Peaking | 5902 Hz |  8.9  | 3.7 dB  |
| Peaking | 6009 Hz |  2.75 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20Primo%208/NuForce%20Primo%208.png)