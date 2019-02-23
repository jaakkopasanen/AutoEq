# House of Marley Liberate XLBT Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.7; 28 -8.8; 31 -8.9; 34 -8.9; 37 -8.9; 41 -9.0; 45 -9.1; 49 -9.2; 54 -9.3; 60 -9.3; 66 -9.5; 72 -9.7; 79 -10.0; 87 -10.2; 96 -10.5; 106 -10.7; 116 -10.8; 128 -11.1; 141 -11.4; 155 -11.6; 170 -11.6; 187 -11.7; 206 -12.0; 227 -12.4; 249 -12.5; 274 -12.5; 302 -12.4; 332 -12.3; 365 -12.0; 402 -11.5; 442 -10.5; 486 -9.4; 535 -8.0; 588 -6.0; 647 -4.8; 712 -5.1; 783 -5.8; 861 -7.4; 947 -8.4; 1042 -9.0; 1146 -9.5; 1261 -9.7; 1387 -9.7; 1526 -9.3; 1678 -7.9; 1846 -6.7; 2031 -3.0; 2234 -2.0; 2457 -4.2; 2703 -4.3; 2973 -3.7; 3270 -3.4; 3597 -1.4; 3957 -0.5; 4353 -1.1; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Liberate XLBT Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Liberate XLBT Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 103 Hz  | 0.26 | -3.3 dB  |
| Peaking | 345 Hz  | 0.68 | -9.3 dB  |
| Peaking | 868 Hz  | 0.35 | 10.1 dB  |
| Peaking | 1249 Hz | 1.19 | -11.5 dB |
| Peaking | 5007 Hz | 1.66 | 5.2 dB   |
| Peaking | 1264 Hz | 6.33 | 1.5 dB   |
| Peaking | 1902 Hz | 1.75 | -2.0 dB  |
| Peaking | 2122 Hz | 7.47 | 5.4 dB   |
| Peaking | 6413 Hz | 4.51 | 3.2 dB   |
| Peaking | 7736 Hz | 1.83 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -6.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Liberate%20XLBT%20Wired/House%20of%20Marley%20Liberate%20XLBT%20Wired.png)