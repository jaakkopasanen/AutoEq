# Campfire Audio Andromeda SS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.4; 25 -4.8; 28 -5.3; 31 -5.7; 34 -6.0; 37 -6.3; 41 -6.6; 45 -7.0; 49 -7.3; 54 -7.7; 60 -8.0; 66 -8.4; 72 -8.8; 79 -9.2; 87 -9.7; 96 -10.2; 106 -10.6; 116 -11.1; 128 -11.4; 141 -11.6; 155 -11.8; 170 -12.0; 187 -12.1; 206 -12.2; 227 -12.2; 249 -12.1; 274 -12.1; 302 -11.9; 332 -11.6; 365 -11.3; 402 -11.1; 442 -10.8; 486 -10.5; 535 -10.2; 588 -9.8; 647 -9.3; 712 -8.8; 783 -8.2; 861 -7.6; 947 -7.2; 1042 -7.1; 1146 -7.1; 1261 -7.0; 1387 -6.5; 1526 -5.9; 1678 -5.4; 1846 -5.0; 2031 -4.1; 2234 -2.4; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.2; 15026 -22.5; 16529 -26.6; 18182 -21.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda SS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda SS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.6  | 4.0 dB   |
| Peaking | 184 Hz   | 0.57 | -2.8 dB  |
| Peaking | 799 Hz   | 0.11 | -3.8 dB  |
| Peaking | 3903 Hz  | 0.43 | 9.8 dB   |
| Peaking | 16736 Hz | 1.3  | -22.9 dB |
| Peaking | 1902 Hz  | 2.55 | -1.4 dB  |
| Peaking | 2465 Hz  | 4.37 | 2.0 dB   |
| Peaking | 7939 Hz  | 3.96 | -3.0 dB  |
| Peaking | 12794 Hz | 2.65 | 6.0 dB   |
| Peaking | 14945 Hz | 3.18 | -6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB   |
| Peaking | 62 Hz    | 1.41 | -1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.0 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -20.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Andromeda%20SS/Campfire%20Audio%20Andromeda%20SS.png)