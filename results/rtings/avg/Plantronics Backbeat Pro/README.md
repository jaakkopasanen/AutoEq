# Plantronics Backbeat Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -22.4; 23 -22.1; 25 -20.7; 28 -17.0; 31 -14.1; 34 -13.4; 37 -13.6; 41 -13.5; 45 -13.0; 49 -12.5; 54 -11.8; 60 -10.9; 66 -10.1; 72 -9.1; 79 -7.6; 87 -5.5; 96 -3.1; 106 -2.8; 116 -3.9; 128 -4.6; 141 -4.3; 155 -3.3; 170 -1.7; 187 -0.5; 206 -0.5; 227 -1.3; 249 -2.0; 274 -2.5; 302 -2.8; 332 -2.6; 365 -2.5; 402 -2.5; 442 -2.3; 486 -2.5; 535 -3.0; 588 -3.1; 647 -3.3; 712 -3.5; 783 -3.6; 861 -3.1; 947 -3.4; 1042 -3.6; 1146 -3.7; 1261 -3.6; 1387 -3.9; 1526 -3.8; 1678 -3.6; 1846 -5.5; 2031 -6.6; 2234 -6.3; 2457 -5.7; 2703 -5.5; 2973 -5.6; 3270 -5.7; 3597 -7.1; 3957 -9.5; 4353 -10.2; 4788 -8.2; 5267 -6.0; 5793 -3.6; 6373 -5.2; 7010 -6.6; 7711 -9.1; 8482 -9.9; 9330 -8.9; 10263 -8.9; 11289 -10.8; 12418 -13.1; 13660 -15.3; 15026 -14.9; 16529 -10.5; 18182 -6.5; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics Backbeat Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics Backbeat Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.51 | -19.0 dB |
| Peaking | 50 Hz    | 1.91 | -6.3 dB  |
| Peaking | 4136 Hz  | 2.89 | -6.0 dB  |
| Peaking | 8261 Hz  | 4.44 | -3.7 dB  |
| Peaking | 14192 Hz | 1.04 | -12.4 dB |
| Peaking | 72 Hz    | 3.59 | -2.1 dB  |
| Peaking | 99 Hz    | 6.03 | 2.8 dB   |
| Peaking | 201 Hz   | 3.02 | 3.4 dB   |
| Peaking | 1166 Hz  | 0.15 | 0.6 dB   |
| Peaking | 2131 Hz  | 2.53 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -15.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB   |
| Peaking | 250 Hz   | 1.41 | 2.1 dB   |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 16000 Hz | 1.41 | -13.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20Backbeat%20Pro/Plantronics%20Backbeat%20Pro.png)