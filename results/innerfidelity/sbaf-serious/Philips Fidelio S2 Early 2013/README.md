# Philips Fidelio S2 Early 2013
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.1; 25 -4.2; 28 -4.3; 31 -4.4; 34 -4.5; 37 -4.6; 41 -4.7; 45 -4.8; 49 -4.8; 54 -5.0; 60 -5.2; 66 -5.4; 72 -5.5; 79 -5.8; 87 -6.0; 96 -6.2; 106 -6.3; 116 -6.3; 128 -6.4; 141 -6.3; 155 -6.3; 170 -6.2; 187 -6.0; 206 -5.8; 227 -5.5; 249 -5.3; 274 -5.0; 302 -4.7; 332 -4.4; 365 -4.1; 402 -3.9; 442 -3.5; 486 -3.4; 535 -3.1; 588 -2.7; 647 -2.6; 712 -2.6; 783 -2.6; 861 -3.0; 947 -3.4; 1042 -4.0; 1146 -4.5; 1261 -5.0; 1387 -5.8; 1526 -6.6; 1678 -7.2; 1846 -7.3; 2031 -7.1; 2234 -6.7; 2457 -5.7; 2703 -4.4; 2973 -2.8; 3270 -1.5; 3597 -1.3; 3957 -2.8; 4353 -6.0; 4788 -7.7; 5267 -6.0; 5793 -3.0; 6373 -0.5; 7010 -1.7; 7711 -3.9; 8482 -4.2; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio S2 Early 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio S2 Early 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 121 Hz  | 0.97 | -2.4 dB |
| Peaking | 1923 Hz | 2.25 | -3.7 dB |
| Peaking | 3535 Hz | 2.77 | 4.4 dB  |
| Peaking | 4742 Hz | 3.49 | -4.9 dB |
| Peaking | 6452 Hz | 4.85 | 4.8 dB  |
| Peaking | 227 Hz  | 1.86 | -0.7 dB |
| Peaking | 736 Hz  | 1.01 | 2.2 dB  |
| Peaking | 1183 Hz | 1.22 | -0.8 dB |
| Peaking | 1486 Hz | 5.18 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20S2%20Early%202013/Philips%20Fidelio%20S2%20Early%202013.png)