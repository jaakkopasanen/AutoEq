# Beyerdynamic DT880 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -0.9; 45 -1.1; 49 -1.3; 54 -1.5; 60 -1.8; 66 -2.1; 72 -2.2; 79 -2.0; 87 -2.5; 96 -3.7; 106 -4.4; 116 -4.9; 128 -5.3; 141 -5.7; 155 -6.0; 170 -6.2; 187 -6.4; 206 -6.6; 227 -6.7; 249 -6.7; 274 -6.6; 302 -6.5; 332 -6.4; 365 -6.3; 402 -6.2; 442 -6.2; 486 -5.9; 535 -5.7; 588 -5.9; 647 -5.8; 712 -5.7; 783 -5.7; 861 -6.2; 947 -6.5; 1042 -6.5; 1146 -6.3; 1261 -6.3; 1387 -6.4; 1526 -6.4; 1678 -6.6; 1846 -6.7; 2031 -6.7; 2234 -6.8; 2457 -7.3; 2703 -8.2; 2973 -8.5; 3270 -7.9; 3597 -7.2; 3957 -7.6; 4353 -7.2; 4788 -6.6; 5267 -8.5; 5793 -12.9; 6373 -11.8; 7010 -8.6; 7711 -8.0; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -8.1; 12418 -8.8; 13660 -7.0; 15026 -7.4; 16529 -11.9; 18182 -15.7; 20000 -17.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT880 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT880 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.49 | 6.4 dB   |
| Peaking | 2904 Hz  | 2.51 | -2.3 dB  |
| Peaking | 6046 Hz  | 4.45 | -7.3 dB  |
| Peaking | 6361 Hz  | 0.12 | 0.6 dB   |
| Peaking | 19331 Hz | 0.73 | -11.8 dB |
| Peaking | 82 Hz    | 4.55 | 1.5 dB   |
| Peaking | 189 Hz   | 1.45 | -0.9 dB  |
| Peaking | 12171 Hz | 4.7  | -2.1 dB  |
| Peaking | 14530 Hz | 2.44 | 2.6 dB   |
| Peaking | 17110 Hz | 2.69 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20880%20250%20Ohm/Beyerdynamic%20DT880%20250%20Ohm.png)