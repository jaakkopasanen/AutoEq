# Bluedio T2S Turbine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -14.3; 25 -14.8; 28 -15.4; 31 -15.7; 34 -15.7; 37 -15.6; 41 -15.5; 45 -15.4; 49 -15.2; 54 -15.1; 60 -15.0; 66 -15.0; 72 -15.0; 79 -15.1; 87 -15.2; 96 -15.3; 106 -15.3; 116 -15.4; 128 -15.6; 141 -15.7; 155 -15.7; 170 -15.7; 187 -15.4; 206 -15.1; 227 -14.8; 249 -14.4; 274 -14.1; 302 -13.6; 332 -13.0; 365 -12.1; 402 -10.9; 442 -9.9; 486 -9.1; 535 -8.1; 588 -6.8; 647 -5.3; 712 -3.5; 783 -1.8; 861 -0.5; 947 -0.5; 1042 -1.4; 1146 -2.4; 1261 -1.7; 1387 -2.8; 1526 -2.7; 1678 -3.1; 1846 -4.0; 2031 -5.0; 2234 -5.3; 2457 -5.0; 2703 -4.7; 2973 -4.2; 3270 -2.6; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -6.5; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T2S Turbine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T2S Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.62 | -7.0 dB |
| Peaking | 189 Hz  | 0.3  | -8.9 dB |
| Peaking | 896 Hz  | 0.97 | 8.9 dB  |
| Peaking | 4453 Hz | 1.7  | 6.7 dB  |
| Peaking | 1652 Hz | 2.8  | 2.2 dB  |
| Peaking | 1933 Hz | 1.26 | -1.4 dB |
| Peaking | 3543 Hz | 6.4  | 2.0 dB  |
| Peaking | 5698 Hz | 5.49 | 5.3 dB  |
| Peaking | 5882 Hz | 1.96 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | -7.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20T2S%20Turbine/Bluedio%20T2S%20Turbine.png)