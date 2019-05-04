# Sennheiser MM 550-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.3; 87 -2.3; 96 -3.0; 106 -3.3; 116 -3.6; 128 -3.6; 141 -3.6; 155 -3.4; 170 -3.3; 187 -3.3; 206 -3.3; 227 -3.2; 249 -3.2; 274 -3.3; 302 -3.3; 332 -3.4; 365 -3.8; 402 -4.2; 442 -4.5; 486 -5.3; 535 -6.2; 588 -7.0; 647 -7.9; 712 -8.9; 783 -9.6; 861 -9.7; 947 -9.5; 1042 -9.1; 1146 -8.8; 1261 -8.6; 1387 -8.8; 1526 -9.3; 1678 -10.3; 1846 -13.0; 2031 -16.6; 2234 -17.3; 2457 -14.3; 2703 -11.7; 2973 -9.3; 3270 -6.4; 3597 -3.1; 3957 -0.6; 4353 -0.5; 4788 -2.3; 5267 -1.7; 5793 -2.3; 6373 -4.9; 7010 -4.8; 7711 -8.0; 8482 -11.2; 9330 -9.1; 10263 -8.6; 11289 -14.2; 12418 -15.2; 13660 -9.7; 15026 -6.5; 16529 -6.9; 18182 -9.1; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 550-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 550-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.36 | 6.4 dB   |
| Peaking | 283 Hz   | 1.47 | 2.9 dB   |
| Peaking | 2272 Hz  | 1.44 | -12.1 dB |
| Peaking | 4122 Hz  | 1.41 | 9.2 dB   |
| Peaking | 11911 Hz | 2.28 | -9.5 dB  |
| Peaking | 817 Hz   | 2.76 | -2.9 dB  |
| Peaking | 1559 Hz  | 4.52 | 2.0 dB   |
| Peaking | 8407 Hz  | 6.21 | -5.3 dB  |
| Peaking | 13784 Hz | 0.37 | 1.2 dB   |
| Peaking | 19264 Hz | 1.16 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 5.0 dB   |
| Peaking | 125 Hz   | 1.41 | 1.3 dB   |
| Peaking | 250 Hz   | 1.41 | 3.5 dB   |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -10.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 16000 Hz | 1.41 | -3.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20MM%20550-X/Sennheiser%20MM%20550-X.png)