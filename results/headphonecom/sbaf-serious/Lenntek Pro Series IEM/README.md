# Lenntek Pro Series IEM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.8; 54 -1.0; 60 -1.3; 66 -1.6; 72 -2.1; 79 -2.4; 87 -2.7; 96 -3.0; 106 -3.3; 116 -3.7; 128 -4.0; 141 -4.3; 155 -4.5; 170 -4.7; 187 -4.8; 206 -5.1; 227 -5.2; 249 -5.2; 274 -5.2; 302 -5.1; 332 -5.2; 365 -5.0; 402 -5.0; 442 -5.1; 486 -5.0; 535 -5.0; 588 -5.0; 647 -5.0; 712 -5.0; 783 -5.3; 861 -5.6; 947 -6.2; 1042 -6.8; 1146 -7.3; 1261 -7.8; 1387 -8.6; 1526 -9.9; 1678 -11.3; 1846 -12.5; 2031 -13.3; 2234 -12.9; 2457 -10.5; 2703 -7.3; 2973 -4.6; 3270 -3.2; 3597 -3.0; 3957 -6.3; 4353 -11.5; 4788 -8.5; 5267 -2.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.8; 8482 -9.1; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lenntek Pro Series IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lenntek Pro Series IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.12 | 6.1 dB  |
| Peaking | 2062 Hz | 2.11 | -8.2 dB |
| Peaking | 3395 Hz | 2.43 | 5.9 dB  |
| Peaking | 4443 Hz | 5.22 | -8.3 dB |
| Peaking | 5798 Hz | 3.81 | 7.5 dB  |
| Peaking | 148 Hz  | 1.24 | -0.6 dB |
| Peaking | 608 Hz  | 0.91 | 1.6 dB  |
| Peaking | 1529 Hz | 3.28 | -1.0 dB |
| Peaking | 6709 Hz | 7.06 | 2.2 dB  |
| Peaking | 8221 Hz | 4.93 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.9 dB  |
| Peaking | 125 Hz   | 1.41 | 1.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Lenntek%20Pro%20Series%20IEM/Lenntek%20Pro%20Series%20IEM.png)