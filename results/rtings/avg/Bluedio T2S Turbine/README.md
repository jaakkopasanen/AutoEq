# Bluedio T2S Turbine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.3; 23 -14.0; 25 -14.5; 28 -15.1; 31 -15.4; 34 -15.5; 37 -15.4; 41 -15.3; 45 -15.1; 49 -15.0; 54 -14.9; 60 -14.8; 66 -14.8; 72 -14.8; 79 -14.8; 87 -14.9; 96 -15.0; 106 -15.1; 116 -15.2; 128 -15.4; 141 -15.5; 155 -15.5; 170 -15.4; 187 -15.3; 206 -15.0; 227 -14.7; 249 -14.4; 274 -14.0; 302 -13.5; 332 -13.0; 365 -12.1; 402 -10.8; 442 -9.9; 486 -9.2; 535 -8.1; 588 -6.9; 647 -5.4; 712 -3.6; 783 -1.9; 861 -0.6; 947 -0.5; 1042 -1.5; 1146 -2.5; 1261 -2.0; 1387 -2.9; 1526 -2.9; 1678 -3.3; 1846 -4.3; 2031 -5.4; 2234 -6.1; 2457 -5.9; 2703 -5.2; 2973 -4.2; 3270 -2.4; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.7; 6373 -5.6; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T2S Turbine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T2S Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.6  | -7.1 dB |
| Peaking | 189 Hz  | 0.34 | -8.6 dB |
| Peaking | 900 Hz  | 1.1  | 8.4 dB  |
| Peaking | 4481 Hz | 1.68 | 6.8 dB  |
| Peaking | 1656 Hz | 3.14 | 1.7 dB  |
| Peaking | 2262 Hz | 2.86 | -1.1 dB |
| Peaking | 3508 Hz | 3.84 | 3.2 dB  |
| Peaking | 4622 Hz | 0.68 | -1.9 dB |
| Peaking | 5636 Hz | 5.64 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.9 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20T2S%20Turbine/Bluedio%20T2S%20Turbine.png)