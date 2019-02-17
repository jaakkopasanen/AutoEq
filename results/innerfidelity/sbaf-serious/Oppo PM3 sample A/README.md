# Oppo PM3 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.7; 25 -5.7; 28 -5.7; 31 -5.7; 34 -5.7; 37 -5.7; 41 -5.7; 45 -5.6; 49 -5.6; 54 -5.6; 60 -5.6; 66 -5.6; 72 -5.7; 79 -5.8; 87 -5.9; 96 -6.3; 106 -6.3; 116 -6.1; 128 -5.9; 141 -6.0; 155 -6.5; 170 -5.4; 187 -5.7; 206 -5.9; 227 -5.5; 249 -5.0; 274 -4.4; 302 -4.0; 332 -3.9; 365 -4.1; 402 -4.3; 442 -4.6; 486 -5.2; 535 -5.5; 588 -5.5; 647 -5.7; 712 -6.0; 783 -5.9; 861 -6.0; 947 -6.2; 1042 -6.5; 1146 -6.8; 1261 -6.9; 1387 -7.6; 1526 -8.3; 1678 -9.4; 1846 -10.2; 2031 -9.6; 2234 -9.6; 2457 -8.9; 2703 -7.8; 2973 -6.2; 3270 -5.6; 3597 -5.4; 3957 -4.5; 4353 -4.5; 4788 -2.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.75 | 0.8 dB  |
| Peaking | 61 Hz   | 1.72 | 0.7 dB  |
| Peaking | 349 Hz  | 1.2  | 2.6 dB  |
| Peaking | 1961 Hz | 2.11 | -4.1 dB |
| Peaking | 5542 Hz | 2.35 | 6.8 dB  |
| Peaking | 2578 Hz | 3.97 | -1.8 dB |
| Peaking | 2896 Hz | 1.8  | 1.4 dB  |
| Peaking | 6585 Hz | 5.61 | 3.1 dB  |
| Peaking | 7120 Hz | 1.76 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3%20sample%20A/Oppo%20PM3%20sample%20A.png)