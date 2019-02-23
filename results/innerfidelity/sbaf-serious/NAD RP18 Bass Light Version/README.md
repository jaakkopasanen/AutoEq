# NAD RP18 Bass Light Version
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -1.1; 206 -1.6; 227 -2.2; 249 -4.5; 274 -5.8; 302 -6.6; 332 -7.7; 365 -7.9; 402 -8.4; 442 -9.0; 486 -9.5; 535 -9.0; 588 -9.1; 647 -9.7; 712 -10.2; 783 -10.1; 861 -10.5; 947 -10.1; 1042 -9.8; 1146 -9.5; 1261 -9.7; 1387 -9.9; 1526 -10.2; 1678 -10.7; 1846 -10.0; 2031 -9.6; 2234 -9.8; 2457 -10.6; 2703 -10.1; 2973 -8.7; 3270 -8.3; 3597 -6.8; 3957 -7.6; 4353 -8.7; 4788 -10.4; 5267 -4.1; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.8; 9330 -9.8; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.3; 18182 -7.1; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD RP18 Bass Light Version GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD RP18 Bass Light Version ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 85 Hz   | 0.15 | 6.8 dB  |
| Peaking | 406 Hz  | 1.07 | -4.6 dB |
| Peaking | 1216 Hz | 0.35 | -4.5 dB |
| Peaking | 4792 Hz | 7.33 | -5.4 dB |
| Peaking | 5857 Hz | 3.46 | 8.5 dB  |
| Peaking | 20 Hz   | 2.47 | 1.0 dB  |
| Peaking | 212 Hz  | 2.16 | 1.6 dB  |
| Peaking | 270 Hz  | 3.5  | -1.8 dB |
| Peaking | 8642 Hz | 1.11 | 1.2 dB  |
| Peaking | 9303 Hz | 3.71 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | 5.9 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -3.5 dB |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NAD%20RP18%20Bass%20Light%20Version/NAD%20RP18%20Bass%20Light%20Version.png)