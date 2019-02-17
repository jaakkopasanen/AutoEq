# Koss Pro4AA 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -1.5; 206 -2.5; 227 -3.6; 249 -4.9; 274 -6.2; 302 -7.5; 332 -8.4; 365 -9.6; 402 -10.5; 442 -11.0; 486 -11.1; 535 -11.4; 588 -10.3; 647 -9.7; 712 -8.9; 783 -7.9; 861 -7.3; 947 -6.6; 1042 -6.3; 1146 -6.3; 1261 -6.9; 1387 -8.4; 1526 -10.4; 1678 -12.4; 1846 -14.2; 2031 -16.2; 2234 -17.9; 2457 -16.9; 2703 -14.0; 2973 -9.6; 3270 -5.7; 3597 -3.5; 3957 -4.4; 4353 -6.6; 4788 -6.4; 5267 -3.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.4; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Pro4AA 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4AA 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 175 Hz  | 0.08 | 7.2 dB   |
| Peaking | 463 Hz  | 0.89 | -11.7 dB |
| Peaking | 2266 Hz | 1.39 | -15.1 dB |
| Peaking | 3471 Hz | 3.35 | 7.1 dB   |
| Peaking | 5961 Hz | 3.75 | 7.3 dB   |
| Peaking | 19 Hz   | 1.76 | 1.4 dB   |
| Peaking | 128 Hz  | 0.06 | -0.4 dB  |
| Peaking | 168 Hz  | 2.61 | 1.8 dB   |
| Peaking | 1158 Hz | 4.02 | 1.5 dB   |
| Peaking | 9557 Hz | 6.16 | -1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 4.0 dB   |
| Peaking | 125 Hz   | 1.41 | 6.0 dB   |
| Peaking | 250 Hz   | 1.41 | 1.8 dB   |
| Peaking | 500 Hz   | 1.41 | -6.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4AA%202014/Koss%20Pro4AA%202014.png)