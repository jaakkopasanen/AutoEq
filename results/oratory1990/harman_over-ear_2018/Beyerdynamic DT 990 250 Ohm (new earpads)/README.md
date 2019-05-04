# Beyerdynamic DT 990 250 Ohm (new earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.4; 31 -3.0; 34 -3.5; 37 -4.0; 41 -4.6; 45 -5.0; 49 -5.4; 54 -5.9; 60 -6.3; 66 -6.7; 72 -7.0; 79 -7.2; 87 -7.1; 96 -7.2; 106 -7.9; 116 -8.3; 128 -8.5; 141 -8.6; 155 -8.5; 170 -8.3; 187 -8.2; 206 -8.0; 227 -7.5; 249 -7.0; 274 -6.4; 302 -5.8; 332 -5.2; 365 -4.5; 402 -4.2; 442 -4.7; 486 -4.3; 535 -3.8; 588 -3.4; 647 -3.2; 712 -3.0; 783 -3.2; 861 -3.7; 947 -4.6; 1042 -5.1; 1146 -5.5; 1261 -5.8; 1387 -5.8; 1526 -5.3; 1678 -5.2; 1846 -5.0; 2031 -5.1; 2234 -5.5; 2457 -6.2; 2703 -7.1; 2973 -7.4; 3270 -6.7; 3597 -6.2; 3957 -7.0; 4353 -7.3; 4788 -8.0; 5267 -10.0; 5793 -12.5; 6373 -10.6; 7010 -7.6; 7711 -10.5; 8482 -11.8; 9330 -9.4; 10263 -9.3; 11289 -13.9; 12418 -18.0; 13660 -16.4; 15026 -13.8; 16529 -16.3; 18182 -19.8; 20000 -20.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 990 250 Ohm (new earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 990 250 Ohm (new earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.59 | 6.0 dB   |
| Peaking | 703 Hz   | 1.05 | 3.6 dB   |
| Peaking | 12644 Hz | 3.92 | -6.9 dB  |
| Peaking | 16052 Hz | 0.2  | -3.5 dB  |
| Peaking | 19372 Hz | 0.62 | -12.0 dB |
| Peaking | 145 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1963 Hz  | 3.54 | 1.7 dB   |
| Peaking | 3843 Hz  | 3.41 | 1.2 dB   |
| Peaking | 5773 Hz  | 7.03 | -4.4 dB  |
| Peaking | 9981 Hz  | 8.5  | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB   |
| Peaking | 62 Hz    | 1.41 | -0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 3.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 16000 Hz | 1.41 | -15.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20990%20250%20Ohm%20(new%20earpads)/Beyerdynamic%20DT%20990%20250%20Ohm%20(new%20earpads).png)