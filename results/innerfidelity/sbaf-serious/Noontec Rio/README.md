# Noontec Rio
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.3; 23 -17.1; 25 -16.9; 28 -16.5; 31 -16.2; 34 -15.9; 37 -15.6; 41 -15.2; 45 -14.9; 49 -14.6; 54 -14.2; 60 -13.9; 66 -13.6; 72 -13.4; 79 -13.2; 87 -12.9; 96 -12.7; 106 -12.3; 116 -11.9; 128 -11.6; 141 -11.2; 155 -10.8; 170 -10.4; 187 -9.9; 206 -9.4; 227 -8.7; 249 -8.2; 274 -7.7; 302 -7.1; 332 -6.5; 365 -6.0; 402 -5.5; 442 -4.8; 486 -4.5; 535 -4.1; 588 -3.6; 647 -3.4; 712 -2.7; 783 -2.5; 861 -2.8; 947 -3.1; 1042 -3.6; 1146 -4.0; 1261 -4.5; 1387 -5.3; 1526 -6.1; 1678 -6.8; 1846 -7.2; 2031 -7.6; 2234 -8.2; 2457 -9.0; 2703 -10.0; 2973 -10.6; 3270 -9.8; 3597 -8.8; 3957 -10.4; 4353 -14.2; 4788 -12.8; 5267 -5.5; 5793 -0.5; 6373 -0.6; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Rio GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Rio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.36 | -10.8 dB |
| Peaking | 121 Hz  | 1.1  | -3.3 dB  |
| Peaking | 2837 Hz | 3.03 | -4.3 dB  |
| Peaking | 4534 Hz | 3.93 | -10.1 dB |
| Peaking | 5949 Hz | 3.46 | 8.3 dB   |
| Peaking | 71 Hz   | 3.39 | -0.6 dB  |
| Peaking | 227 Hz  | 1.76 | -1.2 dB  |
| Peaking | 798 Hz  | 0.84 | 3.7 dB   |
| Peaking | 1825 Hz | 1.74 | -1.7 dB  |
| Peaking | 7993 Hz | 5.65 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Rio/Noontec%20Rio.png)