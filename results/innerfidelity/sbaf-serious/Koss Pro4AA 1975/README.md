# Koss Pro4AA 1975
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.0; 66 -2.3; 72 -3.5; 79 -4.7; 87 -5.8; 96 -6.6; 106 -7.4; 116 -8.2; 128 -9.1; 141 -9.7; 155 -10.4; 170 -10.5; 187 -11.0; 206 -11.9; 227 -12.8; 249 -13.7; 274 -14.5; 302 -15.4; 332 -15.6; 365 -15.0; 402 -13.8; 442 -11.7; 486 -9.4; 535 -8.2; 588 -6.8; 647 -4.7; 712 -3.8; 783 -3.3; 861 -4.4; 947 -5.6; 1042 -6.7; 1146 -7.3; 1261 -8.5; 1387 -9.9; 1526 -11.5; 1678 -12.7; 1846 -13.2; 2031 -13.1; 2234 -12.8; 2457 -11.4; 2703 -10.7; 2973 -9.1; 3270 -6.9; 3597 -4.1; 3957 -0.9; 4353 -1.0; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Pro4AA 1975 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4AA 1975 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 38 Hz   | 0.54 | 7.5 dB   |
| Peaking | 361 Hz  | 0.57 | -17.1 dB |
| Peaking | 703 Hz  | 0.55 | 15.7 dB  |
| Peaking | 1983 Hz | 0.65 | -12.0 dB |
| Peaking | 4581 Hz | 1.25 | 10.5 dB  |
| Peaking | 36 Hz   | 2.54 | -0.8 dB  |
| Peaking | 58 Hz   | 4.63 | 1.5 dB   |
| Peaking | 6362 Hz | 4.1  | 3.7 dB   |
| Peaking | 7464 Hz | 1.26 | -1.4 dB  |
| Peaking | 7528 Hz | 3.25 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB   |
| Peaking | 62 Hz    | 1.41 | 4.2 dB   |
| Peaking | 125 Hz   | 1.41 | -1.6 dB  |
| Peaking | 250 Hz   | 1.41 | -8.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4AA%201975/Koss%20Pro4AA%201975.png)