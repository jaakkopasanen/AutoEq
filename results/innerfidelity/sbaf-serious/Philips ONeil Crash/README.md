# Philips ONeil Crash
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -13.8; 25 -14.1; 28 -14.4; 31 -14.7; 34 -14.9; 37 -15.1; 41 -15.2; 45 -15.3; 49 -15.5; 54 -15.6; 60 -15.7; 66 -15.9; 72 -16.1; 79 -16.4; 87 -16.7; 96 -16.9; 106 -16.9; 116 -16.9; 128 -17.4; 141 -17.8; 155 -17.3; 170 -16.5; 187 -16.6; 206 -16.1; 227 -15.4; 249 -14.5; 274 -13.5; 302 -12.7; 332 -12.0; 365 -11.4; 402 -11.1; 442 -10.6; 486 -10.2; 535 -9.8; 588 -8.8; 647 -8.0; 712 -7.0; 783 -6.4; 861 -5.9; 947 -5.4; 1042 -5.2; 1146 -5.3; 1261 -5.5; 1387 -6.4; 1526 -7.3; 1678 -7.7; 1846 -8.7; 2031 -9.8; 2234 -11.3; 2457 -12.5; 2703 -12.6; 2973 -11.7; 3270 -10.0; 3597 -6.8; 3957 -4.5; 4353 -6.8; 4788 -3.2; 5267 -0.5; 5793 -1.6; 6373 -4.9; 7010 -7.9; 7711 -10.0; 8482 -11.3; 9330 -10.5; 10263 -6.1; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.6; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips ONeil Crash GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips ONeil Crash ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.24 | -8.4 dB |
| Peaking | 180 Hz  | 0.53 | -7.9 dB |
| Peaking | 2553 Hz | 2.59 | -8.1 dB |
| Peaking | 8606 Hz | 4.29 | -7.0 dB |
| Peaking | 1037 Hz | 2.81 | 1.7 dB  |
| Peaking | 1839 Hz | 3.98 | -1.3 dB |
| Peaking | 3154 Hz | 8.15 | -2.2 dB |
| Peaking | 5441 Hz | 3.88 | 6.1 dB  |
| Peaking | 7349 Hz | 5.36 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.1 dB  |
| Peaking | 62 Hz    | 1.41 | -7.3 dB  |
| Peaking | 125 Hz   | 1.41 | -10.4 dB |
| Peaking | 250 Hz   | 1.41 | -7.1 dB  |
| Peaking | 500 Hz   | 1.41 | -3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.3 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20ONeil%20Crash/Philips%20ONeil%20Crash.png)