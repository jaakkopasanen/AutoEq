# Lenntek Pro Series IEM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.7; 41 -0.8; 45 -1.1; 49 -1.3; 54 -1.5; 60 -1.8; 66 -2.2; 72 -2.6; 79 -2.9; 87 -3.2; 96 -3.5; 106 -3.8; 116 -4.2; 128 -4.5; 141 -4.8; 155 -5.1; 170 -5.3; 187 -5.4; 206 -5.7; 227 -5.7; 249 -5.8; 274 -5.7; 302 -5.6; 332 -5.7; 365 -5.6; 402 -5.5; 442 -5.6; 486 -5.5; 535 -5.6; 588 -5.5; 647 -5.5; 712 -5.6; 783 -5.8; 861 -6.2; 947 -6.7; 1042 -7.3; 1146 -7.8; 1261 -8.3; 1387 -9.1; 1526 -10.5; 1678 -11.9; 1846 -13.0; 2031 -13.8; 2234 -13.4; 2457 -11.1; 2703 -7.8; 2973 -5.2; 3270 -3.7; 3597 -3.6; 3957 -6.8; 4353 -12.0; 4788 -9.0; 5267 -2.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.3; 8482 -9.7; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lenntek Pro Series IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lenntek Pro Series IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.24 | 6.1 dB  |
| Peaking | 2057 Hz | 1.88 | -8.6 dB |
| Peaking | 3364 Hz | 2.44 | 5.9 dB  |
| Peaking | 4398 Hz | 5.12 | -8.4 dB |
| Peaking | 5799 Hz | 4.05 | 7.6 dB  |
| Peaking | 629 Hz  | 1.29 | 1.2 dB  |
| Peaking | 1517 Hz | 3.75 | -0.8 dB |
| Peaking | 6747 Hz | 7.29 | 2.6 dB  |
| Peaking | 8260 Hz | 4.77 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Lenntek%20Pro%20Series%20IEM/Lenntek%20Pro%20Series%20IEM.png)