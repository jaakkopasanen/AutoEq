# Ambient Acoustics AM7 Blue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.7; 25 -6.1; 28 -6.6; 31 -7.0; 34 -7.2; 37 -7.5; 41 -7.7; 45 -7.9; 49 -8.2; 54 -8.4; 60 -8.7; 66 -8.9; 72 -9.2; 79 -9.5; 87 -9.8; 96 -10.1; 106 -10.5; 116 -10.8; 128 -10.9; 141 -11.1; 155 -11.1; 170 -11.1; 187 -11.2; 206 -11.1; 227 -10.9; 249 -10.7; 274 -10.4; 302 -10.0; 332 -9.5; 365 -8.9; 402 -8.4; 442 -7.9; 486 -7.3; 535 -6.6; 588 -5.9; 647 -5.3; 712 -4.6; 783 -4.0; 861 -3.6; 947 -3.7; 1042 -4.2; 1146 -5.0; 1261 -5.9; 1387 -6.5; 1526 -7.0; 1678 -8.3; 1846 -11.1; 2031 -12.1; 2234 -8.5; 2457 -4.9; 2703 -3.2; 2973 -4.0; 3270 -6.8; 3597 -2.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.4; 5793 -2.5; 6373 -4.1; 7010 -7.4; 7711 -8.3; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -17.0; 16529 -28.7; 18182 -35.3; 20000 -26.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ambient Acoustics AM7 Blue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ambient Acoustics AM7 Blue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 170 Hz   | 0.47 | -4.9 dB  |
| Peaking | 795 Hz   | 1.82 | 2.8 dB   |
| Peaking | 1941 Hz  | 3.44 | -9.0 dB  |
| Peaking | 10760 Hz | 0.22 | 18.9 dB  |
| Peaking | 18072 Hz | 0.4  | -42.8 dB |
| Peaking | 18 Hz    | 2.21 | 1.7 dB   |
| Peaking | 4538 Hz  | 3.41 | 3.4 dB   |
| Peaking | 7586 Hz  | 3.1  | -5.0 dB  |
| Peaking | 13585 Hz | 2.76 | 7.0 dB   |
| Peaking | 16286 Hz | 2.43 | -5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB   |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 16000 Hz | 1.41 | -23.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ambient%20Acoustics%20AM7%20Blue/Ambient%20Acoustics%20AM7%20Blue.png)