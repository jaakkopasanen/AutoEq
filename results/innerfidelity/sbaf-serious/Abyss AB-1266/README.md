# Abyss AB-1266
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -4.3; 25 -5.0; 28 -5.7; 31 -5.8; 34 -5.7; 37 -5.5; 41 -5.6; 45 -6.1; 49 -6.4; 54 -6.2; 60 -5.7; 66 -5.6; 72 -5.5; 79 -5.6; 87 -5.7; 96 -5.9; 106 -6.0; 116 -6.1; 128 -6.4; 141 -6.5; 155 -6.7; 170 -6.8; 187 -6.9; 206 -7.1; 227 -7.1; 249 -7.4; 274 -7.5; 302 -7.9; 332 -8.3; 365 -8.2; 402 -8.7; 442 -9.0; 486 -5.9; 535 -5.9; 588 -6.4; 647 -7.7; 712 -8.8; 783 -9.6; 861 -11.0; 947 -11.5; 1042 -10.6; 1146 -10.3; 1261 -9.4; 1387 -8.8; 1526 -8.3; 1678 -6.8; 1846 -5.0; 2031 -4.9; 2234 -5.6; 2457 -5.3; 2703 -3.6; 2973 -2.9; 3270 -3.2; 3597 -2.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.9; 6373 -7.7; 7010 -8.2; 7711 -7.8; 8482 -10.6; 9330 -12.3; 10263 -9.4; 11289 -7.3; 12418 -8.7; 13660 -10.1; 15026 -10.1; 16529 -11.1; 18182 -13.2; 20000 -13.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Abyss AB-1266 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Abyss AB-1266 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 348 Hz   | 2.44 | -1.9 dB |
| Peaking | 985 Hz   | 2.01 | -5.2 dB |
| Peaking | 4459 Hz  | 1.23 | 9.2 dB  |
| Peaking | 20028 Hz | 0.05 | -5.1 dB |
| Peaking | 531 Hz   | 7.1  | 2.0 dB  |
| Peaking | 9344 Hz  | 4.15 | -3.5 dB |
| Peaking | 9356 Hz  | 1.55 | -2.2 dB |
| Peaking | 11067 Hz | 1.91 | 4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Abyss%20AB-1266/Abyss%20AB-1266.png)