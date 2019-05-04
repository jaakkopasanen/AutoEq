# Beyerdynamic DT 770 250 Ohm (old earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.4; 25 -6.6; 28 -6.9; 31 -7.0; 34 -7.0; 37 -7.0; 41 -6.8; 45 -6.4; 49 -5.9; 54 -4.9; 60 -3.5; 66 -2.1; 72 -1.4; 79 -1.5; 87 -2.8; 96 -5.1; 106 -6.6; 116 -7.2; 128 -7.3; 141 -6.4; 155 -5.6; 170 -4.6; 187 -3.3; 206 -2.5; 227 -2.9; 249 -3.7; 274 -4.6; 302 -5.2; 332 -5.6; 365 -5.8; 402 -5.9; 442 -6.0; 486 -6.1; 535 -6.0; 588 -5.7; 647 -5.7; 712 -5.8; 783 -5.6; 861 -5.5; 947 -5.4; 1042 -5.3; 1146 -5.4; 1261 -5.3; 1387 -5.1; 1526 -5.0; 1678 -4.8; 1846 -4.8; 2031 -5.4; 2234 -6.0; 2457 -5.9; 2703 -4.7; 2973 -2.4; 3270 -0.5; 3597 -1.1; 3957 -3.6; 4353 -4.4; 4788 -4.7; 5267 -5.4; 5793 -7.5; 6373 -10.4; 7010 -9.3; 7711 -8.4; 8482 -7.8; 9330 -6.4; 10263 -5.4; 11289 -8.0; 12418 -12.4; 13660 -12.6; 15026 -10.5; 16529 -12.0; 18182 -14.2; 20000 -13.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 250 Ohm (old earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 250 Ohm (old earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 74 Hz    | 4.33 | 4.7 dB  |
| Peaking | 3401 Hz  | 3.73 | 5.5 dB  |
| Peaking | 6624 Hz  | 3.98 | -4.9 dB |
| Peaking | 13045 Hz | 3.64 | -6.0 dB |
| Peaking | 18799 Hz | 0.63 | -9.5 dB |
| Peaking | 33 Hz    | 2.11 | -1.9 dB |
| Peaking | 122 Hz   | 3.67 | -2.7 dB |
| Peaking | 210 Hz   | 3.44 | 3.2 dB  |
| Peaking | 2383 Hz  | 7.1  | -1.5 dB |
| Peaking | 10287 Hz | 7.65 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | 3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -9.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20770%20250%20Ohm%20(old%20earpads)/Beyerdynamic%20DT%20770%20250%20Ohm%20(old%20earpads).png)