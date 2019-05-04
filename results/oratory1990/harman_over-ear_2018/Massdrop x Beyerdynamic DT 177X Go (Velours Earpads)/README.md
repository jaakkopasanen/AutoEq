# Massdrop x Beyerdynamic DT 177X Go (Velours Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.4; 25 -10.7; 28 -11.0; 31 -11.3; 34 -11.4; 37 -11.4; 41 -11.1; 45 -10.3; 49 -9.6; 54 -9.7; 60 -10.2; 66 -9.0; 72 -8.7; 79 -11.2; 87 -13.4; 96 -14.2; 106 -14.5; 116 -14.7; 128 -14.6; 141 -14.4; 155 -13.9; 170 -13.2; 187 -12.2; 206 -10.9; 227 -9.7; 249 -8.6; 274 -7.9; 302 -7.5; 332 -7.3; 365 -7.1; 402 -7.2; 442 -7.3; 486 -7.3; 535 -7.2; 588 -7.1; 647 -7.0; 712 -6.9; 783 -6.9; 861 -7.0; 947 -7.0; 1042 -6.9; 1146 -6.5; 1261 -5.9; 1387 -5.3; 1526 -4.2; 1678 -2.8; 1846 -1.8; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.8; 3597 -3.4; 3957 -3.0; 4353 -0.5; 4788 -1.9; 5267 -5.0; 5793 -4.2; 6373 -6.3; 7010 -9.7; 7711 -10.4; 8482 -8.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Beyerdynamic DT 177X Go (Velours Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Beyerdynamic DT 177X Go (Velours Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 1.21 | -4.6 dB |
| Peaking | 125 Hz  | 1.02 | -8.6 dB |
| Peaking | 2446 Hz | 1.43 | 6.7 dB  |
| Peaking | 4496 Hz | 4.47 | 4.8 dB  |
| Peaking | 7522 Hz | 4.64 | -5.0 dB |
| Peaking | 72 Hz   | 6.38 | 2.6 dB  |
| Peaking | 89 Hz   | 5.38 | -1.6 dB |
| Peaking | 302 Hz  | 3.1  | 1.0 dB  |
| Peaking | 1045 Hz | 1.17 | -1.1 dB |
| Peaking | 1767 Hz | 3.94 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -9.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Beyerdynamic%20DT%20177X%20Go%20(Velours%20Earpads)/Massdrop%20x%20Beyerdynamic%20DT%20177X%20Go%20(Velours%20Earpads).png)