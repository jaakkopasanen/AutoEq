# Campfire Audio Solaris
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.4; 25 -7.5; 28 -7.7; 31 -7.8; 34 -7.9; 37 -8.0; 41 -8.1; 45 -8.2; 49 -8.3; 54 -8.5; 60 -8.7; 66 -8.9; 72 -9.2; 79 -9.4; 87 -9.7; 96 -10.0; 106 -10.3; 116 -10.6; 128 -10.8; 141 -10.9; 155 -11.1; 170 -11.1; 187 -11.1; 206 -11.1; 227 -11.0; 249 -10.9; 274 -10.7; 302 -10.5; 332 -10.1; 365 -9.8; 402 -9.5; 442 -9.3; 486 -9.0; 535 -8.6; 588 -8.3; 647 -8.0; 712 -7.7; 783 -7.5; 861 -7.5; 947 -7.3; 1042 -7.1; 1146 -7.0; 1261 -7.0; 1387 -6.8; 1526 -6.5; 1678 -6.6; 1846 -7.2; 2031 -7.8; 2234 -6.8; 2457 -4.3; 2703 -1.8; 2973 -0.9; 3270 -1.6; 3597 -1.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -7.8; 11289 -6.8; 12418 -8.0; 13660 -15.8; 15026 -25.0; 16529 -28.8; 18182 -26.7; 20000 -20.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Solaris GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Solaris ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.18 | -0.7 dB  |
| Peaking | 193 Hz   | 0.44 | -4.4 dB  |
| Peaking | 4775 Hz  | 0.65 | 15.1 dB  |
| Peaking | 12273 Hz | 0.78 | 20.6 dB  |
| Peaking | 15679 Hz | 0.31 | -34.2 dB |
| Peaking | 2103 Hz  | 3.96 | -2.9 dB  |
| Peaking | 2802 Hz  | 3.78 | 3.1 dB   |
| Peaking | 4773 Hz  | 3.1  | -1.5 dB  |
| Peaking | 6377 Hz  | 3.33 | 2.2 dB   |
| Peaking | 7467 Hz  | 4.93 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 16000 Hz | 1.41 | -27.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Solaris/Campfire%20Audio%20Solaris.png)