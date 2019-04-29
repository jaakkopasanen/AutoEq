# Satolex Tubomi DH302-A1Bs
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.5; 25 -7.0; 28 -7.6; 31 -8.2; 34 -8.6; 37 -9.0; 41 -9.4; 45 -9.7; 49 -10.0; 54 -10.4; 60 -10.7; 66 -11.1; 72 -11.4; 79 -11.7; 87 -12.0; 96 -12.3; 106 -12.5; 116 -12.6; 128 -12.6; 141 -12.6; 155 -12.8; 170 -12.7; 187 -12.7; 206 -12.3; 227 -11.9; 249 -11.4; 274 -10.9; 302 -10.3; 332 -9.6; 365 -8.9; 402 -8.3; 442 -7.6; 486 -6.9; 535 -6.2; 588 -5.4; 647 -4.7; 712 -3.9; 783 -3.1; 861 -2.4; 947 -1.9; 1042 -1.8; 1146 -2.1; 1261 -2.3; 1387 -2.2; 1526 -1.9; 1678 -1.4; 1846 -1.0; 2031 -0.8; 2234 -1.7; 2457 -2.9; 2703 -2.8; 2973 -2.5; 3270 -1.9; 3597 -1.0; 3957 -0.5; 4353 -1.3; 4788 -3.1; 5267 -6.5; 5793 -6.4; 6373 -1.6; 7010 -2.9; 7711 -5.2; 8482 -5.4; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -9.9; 15026 -22.3; 16529 -25.5; 18182 -22.5; 20000 -17.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Satolex Tubomi DH302-A1Bs GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Satolex Tubomi DH302-A1Bs ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 95 Hz    | 0.43 | -5.7 dB  |
| Peaking | 236 Hz   | 0.69 | -3.7 dB  |
| Peaking | 4302 Hz  | 0.23 | 9.8 dB   |
| Peaking | 12851 Hz | 0.8  | 20.0 dB  |
| Peaking | 15588 Hz | 0.41 | -35.6 dB |
| Peaking | 909 Hz   | 4.91 | 1.1 dB   |
| Peaking | 2645 Hz  | 3.15 | -1.9 dB  |
| Peaking | 4186 Hz  | 2.44 | 3.3 dB   |
| Peaking | 5566 Hz  | 3.08 | -5.3 dB  |
| Peaking | 6571 Hz  | 6.34 | 5.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 16000 Hz | 1.41 | -22.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Satolex%20Tubomi%20DH302-A1Bs/Satolex%20Tubomi%20DH302-A1Bs.png)