# Periodic Audio Be
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.0; 25 -11.0; 28 -10.9; 31 -10.8; 34 -10.8; 37 -10.7; 41 -10.6; 45 -10.6; 49 -10.6; 54 -10.6; 60 -10.5; 66 -10.4; 72 -10.4; 79 -10.4; 87 -10.3; 96 -10.3; 106 -10.3; 116 -10.3; 128 -10.1; 141 -9.9; 155 -9.6; 170 -9.2; 187 -8.7; 206 -8.1; 227 -7.4; 249 -7.2; 274 -7.9; 302 -7.4; 332 -6.6; 365 -6.1; 402 -5.7; 442 -5.3; 486 -4.8; 535 -4.3; 588 -3.9; 647 -3.5; 712 -3.0; 783 -2.7; 861 -2.5; 947 -2.7; 1042 -3.2; 1146 -4.0; 1261 -4.6; 1387 -5.0; 1526 -4.9; 1678 -4.9; 1846 -5.3; 2031 -5.3; 2234 -5.3; 2457 -5.1; 2703 -4.4; 2973 -3.4; 3270 -2.4; 3597 -1.4; 3957 -0.7; 4353 -0.5; 4788 -1.1; 5267 -2.9; 5793 -6.9; 6373 -8.9; 7010 -5.2; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.4; 16529 -8.8; 18182 -12.0; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Be GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Be ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.33 | -5.3 dB |
| Peaking | 121 Hz   | 0.56 | -3.8 dB |
| Peaking | 789 Hz   | 1.49 | 3.1 dB  |
| Peaking | 4079 Hz  | 2.83 | 5.4 dB  |
| Peaking | 18890 Hz | 1.06 | -7.8 dB |
| Peaking | 230 Hz   | 8.54 | 0.6 dB  |
| Peaking | 3231 Hz  | 8.77 | 1.0 dB  |
| Peaking | 4989 Hz  | 7.01 | 2.1 dB  |
| Peaking | 6189 Hz  | 7    | -5.1 dB |
| Peaking | 14221 Hz | 2.4  | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Periodic%20Audio%20Be/Periodic%20Audio%20Be.png)