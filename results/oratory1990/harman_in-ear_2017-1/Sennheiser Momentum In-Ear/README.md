# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.3; 25 -12.4; 28 -12.6; 31 -12.7; 34 -12.7; 37 -12.7; 41 -12.6; 45 -12.6; 49 -12.7; 54 -12.8; 60 -13.0; 66 -13.2; 72 -13.4; 79 -13.7; 87 -13.9; 96 -14.2; 106 -14.4; 116 -14.6; 128 -14.7; 141 -14.7; 155 -14.6; 170 -14.4; 187 -14.2; 206 -13.9; 227 -13.4; 249 -13.0; 274 -12.7; 302 -12.2; 332 -11.4; 365 -10.7; 402 -10.0; 442 -9.3; 486 -8.5; 535 -7.7; 588 -6.8; 647 -6.0; 712 -5.2; 783 -4.3; 861 -3.7; 947 -3.3; 1042 -3.1; 1146 -2.9; 1261 -2.6; 1387 -2.2; 1526 -1.9; 1678 -1.6; 1846 -1.3; 2031 -0.9; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -4.4; 6373 -8.5; 7010 -10.3; 7711 -8.1; 8482 -6.5; 9330 -8.8; 10263 -11.5; 11289 -10.8; 12418 -12.7; 13660 -19.2; 15026 -23.4; 16529 -22.0; 18182 -17.6; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.2  | -5.1 dB  |
| Peaking | 195 Hz   | 0.52 | -5.9 dB  |
| Peaking | 2635 Hz  | 0.37 | 6.8 dB   |
| Peaking | 15983 Hz | 0.72 | -17.6 dB |
| Peaking | 822 Hz   | 4.46 | 0.9 dB   |
| Peaking | 4894 Hz  | 3.16 | 2.6 dB   |
| Peaking | 6727 Hz  | 5.46 | -5.7 dB  |
| Peaking | 11847 Hz | 5.72 | 3.4 dB   |
| Peaking | 19851 Hz | 1.6  | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -6.9 dB  |
| Peaking | 250 Hz   | 1.41 | -5.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -21.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)