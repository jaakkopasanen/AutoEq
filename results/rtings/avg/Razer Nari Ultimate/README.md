# Razer Nari Ultimate
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.8; 25 -4.0; 28 -4.2; 31 -4.4; 34 -4.5; 37 -4.7; 41 -4.9; 45 -5.3; 49 -5.8; 54 -6.4; 60 -6.9; 66 -7.3; 72 -7.6; 79 -8.1; 87 -8.7; 96 -9.4; 106 -10.0; 116 -10.4; 128 -10.6; 141 -10.6; 155 -10.6; 170 -10.6; 187 -10.5; 206 -10.4; 227 -10.2; 249 -10.0; 274 -9.8; 302 -9.2; 332 -8.5; 365 -8.1; 402 -7.8; 442 -7.3; 486 -6.7; 535 -5.9; 588 -5.1; 647 -4.7; 712 -4.5; 783 -4.2; 861 -3.1; 947 -2.3; 1042 -2.6; 1146 -2.4; 1261 -2.6; 1387 -2.0; 1526 -1.4; 1678 -1.0; 1846 -0.8; 2031 -0.7; 2234 -0.5; 2457 -1.1; 2703 -2.4; 2973 -3.6; 3270 -4.8; 3597 -5.4; 3957 -5.6; 4353 -4.5; 4788 -3.9; 5267 -4.4; 5793 -4.9; 6373 -4.9; 7010 -5.6; 7711 -5.3; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.7; 18182 -9.6; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Nari Ultimate GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Nari Ultimate ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.27 | 2.4 dB  |
| Peaking | 153 Hz   | 0.42 | -6.1 dB |
| Peaking | 1046 Hz  | 0.8  | 3.2 dB  |
| Peaking | 2100 Hz  | 1.9  | 4.1 dB  |
| Peaking | 18811 Hz | 1.62 | -5.0 dB |
| Peaking | 2574 Hz  | 5.11 | 0.8 dB  |
| Peaking | 3893 Hz  | 2.44 | -2.1 dB |
| Peaking | 4603 Hz  | 2.75 | 2.1 dB  |
| Peaking | 7248 Hz  | 3.38 | -0.2 dB |
| Peaking | 15536 Hz | 3.22 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Nari%20Ultimate/Razer%20Nari%20Ultimate.png)