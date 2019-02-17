# Philips Fidelio L1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.7; 25 -12.0; 28 -12.4; 31 -12.7; 34 -12.9; 37 -13.1; 41 -13.3; 45 -13.3; 49 -13.4; 54 -13.5; 60 -13.5; 66 -13.6; 72 -13.6; 79 -13.6; 87 -13.6; 96 -13.5; 106 -13.3; 116 -13.1; 128 -13.5; 141 -13.5; 155 -13.3; 170 -12.5; 187 -12.1; 206 -12.1; 227 -12.0; 249 -12.0; 274 -11.7; 302 -11.2; 332 -10.6; 365 -10.1; 402 -9.3; 442 -8.7; 486 -8.4; 535 -7.6; 588 -6.7; 647 -6.1; 712 -5.7; 783 -5.1; 861 -5.2; 947 -5.4; 1042 -5.5; 1146 -5.8; 1261 -6.5; 1387 -8.5; 1526 -10.6; 1678 -12.4; 1846 -13.1; 2031 -12.9; 2234 -13.6; 2457 -13.6; 2703 -12.7; 2973 -11.1; 3270 -8.6; 3597 -7.0; 3957 -5.8; 4353 -4.4; 4788 -2.4; 5267 -0.5; 5793 -0.5; 6373 -2.2; 7010 -7.7; 7711 -9.4; 8482 -9.3; 9330 -6.0; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -6.1; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio L1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio L1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.36 | -7.6 dB |
| Peaking | 147 Hz  | 0.94 | -3.8 dB |
| Peaking | 298 Hz  | 1.56 | -3.6 dB |
| Peaking | 2238 Hz | 1.53 | -9.0 dB |
| Peaking | 5320 Hz | 3.74 | 6.7 dB  |
| Peaking | 1038 Hz | 1.52 | 2.0 dB  |
| Peaking | 1622 Hz | 4.89 | -2.8 dB |
| Peaking | 6199 Hz | 5.66 | 3.6 dB  |
| Peaking | 7905 Hz | 2.66 | -5.7 dB |
| Peaking | 9682 Hz | 2.63 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -6.2 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20L1/Philips%20Fidelio%20L1.png)