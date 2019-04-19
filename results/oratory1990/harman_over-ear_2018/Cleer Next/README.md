# Cleer Next
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.1; 25 -2.2; 28 -2.4; 31 -2.6; 34 -2.7; 37 -2.8; 41 -3.0; 45 -3.1; 49 -3.1; 54 -3.2; 60 -3.3; 66 -3.5; 72 -3.7; 79 -4.0; 87 -4.4; 96 -5.0; 106 -5.5; 116 -5.9; 128 -6.3; 141 -6.6; 155 -6.8; 170 -6.9; 187 -6.9; 206 -6.9; 227 -6.7; 249 -6.5; 274 -6.2; 302 -5.9; 332 -5.4; 365 -4.9; 402 -4.5; 442 -4.1; 486 -3.6; 535 -3.1; 588 -2.8; 647 -2.4; 712 -2.2; 783 -2.0; 861 -1.4; 947 -1.7; 1042 -2.0; 1146 -2.0; 1261 -2.1; 1387 -2.3; 1526 -2.8; 1678 -3.2; 1846 -3.8; 2031 -4.6; 2234 -5.2; 2457 -5.1; 2703 -5.1; 2973 -4.9; 3270 -4.3; 3597 -3.0; 3957 -1.3; 4353 -3.3; 4788 -6.7; 5267 -5.1; 5793 -3.2; 6373 -0.5; 7010 -1.3; 7711 -3.6; 8482 -3.8; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -7.8; 20000 -14.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cleer Next GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cleer Next ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.12 | 1.7 dB   |
| Peaking | 175 Hz   | 0.71 | -3.7 dB  |
| Peaking | 848 Hz   | 1.22 | 2.7 dB   |
| Peaking | 6566 Hz  | 7.34 | 4.2 dB   |
| Peaking | 19700 Hz | 1.4  | -10.2 dB |
| Peaking | 1456 Hz  | 2.23 | 1.1 dB   |
| Peaking | 2504 Hz  | 1.48 | -2.0 dB  |
| Peaking | 4095 Hz  | 3.9  | 4.4 dB   |
| Peaking | 4697 Hz  | 5.29 | -4.7 dB  |
| Peaking | 16035 Hz | 2.03 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Cleer%20Next/Cleer%20Next.png)