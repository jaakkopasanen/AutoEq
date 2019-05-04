# Massdrop x Beyerdynamic DT 177X Go (Leather Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.9; 25 -10.2; 28 -10.4; 31 -10.6; 34 -10.7; 37 -10.7; 41 -10.7; 45 -10.8; 49 -10.9; 54 -11.0; 60 -11.0; 66 -10.8; 72 -10.6; 79 -10.7; 87 -11.3; 96 -12.4; 106 -13.2; 116 -13.8; 128 -13.8; 141 -13.6; 155 -13.0; 170 -12.2; 187 -11.3; 206 -10.0; 227 -8.7; 249 -7.5; 274 -6.8; 302 -6.7; 332 -6.6; 365 -6.4; 402 -6.3; 442 -6.5; 486 -6.6; 535 -6.8; 588 -7.0; 647 -7.2; 712 -7.2; 783 -7.2; 861 -7.2; 947 -7.2; 1042 -7.1; 1146 -7.0; 1261 -6.7; 1387 -6.2; 1526 -5.6; 1678 -4.5; 1846 -3.5; 2031 -2.6; 2234 -1.7; 2457 -0.6; 2703 -0.5; 2973 -1.2; 3270 -3.2; 3597 -4.4; 3957 -4.8; 4353 -4.4; 4788 -3.8; 5267 -2.8; 5793 -0.6; 6373 -2.1; 7010 -6.5; 7711 -8.8; 8482 -7.8; 9330 -6.5; 10263 -6.5; 11289 -7.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Beyerdynamic DT 177X Go (Leather Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Beyerdynamic DT 177X Go (Leather Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.59 | -3.6 dB |
| Peaking | 132 Hz  | 1.39 | -6.8 dB |
| Peaking | 2568 Hz | 1.98 | 6.4 dB  |
| Peaking | 5792 Hz | 5.23 | 6.2 dB  |
| Peaking | 15 Hz   | 0.55 | -1.1 dB |
| Peaking | 195 Hz  | 2.97 | -1.7 dB |
| Peaking | 273 Hz  | 1.12 | 1.4 dB  |
| Peaking | 879 Hz  | 1.47 | -1.1 dB |
| Peaking | 7842 Hz | 6.11 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Beyerdynamic%20DT%20177X%20Go%20(Leather%20Earpads)/Massdrop%20x%20Beyerdynamic%20DT%20177X%20Go%20(Leather%20Earpads).png)