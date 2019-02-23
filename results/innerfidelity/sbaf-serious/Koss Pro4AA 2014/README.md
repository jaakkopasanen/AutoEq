# Koss Pro4AA 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.7; 187 -1.7; 206 -2.8; 227 -3.8; 249 -5.1; 274 -6.5; 302 -7.7; 332 -8.6; 365 -9.8; 402 -10.8; 442 -11.2; 486 -11.3; 535 -11.6; 588 -10.5; 647 -9.9; 712 -9.2; 783 -8.2; 861 -7.6; 947 -6.8; 1042 -6.5; 1146 -6.5; 1261 -7.1; 1387 -8.6; 1526 -10.6; 1678 -12.6; 1846 -14.4; 2031 -16.4; 2234 -18.1; 2457 -17.1; 2703 -14.2; 2973 -9.8; 3270 -5.9; 3597 -3.7; 3957 -4.6; 4353 -6.8; 4788 -6.6; 5267 -3.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.6; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Pro4AA 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4AA 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 173 Hz  | 0.08 | 7.2 dB   |
| Peaking | 464 Hz  | 0.87 | -11.9 dB |
| Peaking | 2268 Hz | 1.36 | -15.3 dB |
| Peaking | 3482 Hz | 3.37 | 7.1 dB   |
| Peaking | 6006 Hz | 3.82 | 7.4 dB   |
| Peaking | 19 Hz   | 1.24 | 1.6 dB   |
| Peaking | 86 Hz   | 0.22 | -0.7 dB  |
| Peaking | 161 Hz  | 2.18 | 1.8 dB   |
| Peaking | 1162 Hz | 4.69 | 1.3 dB   |
| Peaking | 9459 Hz | 6.4  | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 4.0 dB   |
| Peaking | 125 Hz   | 1.41 | 6.1 dB   |
| Peaking | 250 Hz   | 1.41 | 1.6 dB   |
| Peaking | 500 Hz   | 1.41 | -6.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4AA%202014/Koss%20Pro4AA%202014.png)