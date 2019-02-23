# Marshall Major
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.3; 87 -1.6; 96 -1.8; 106 -2.5; 116 -3.1; 128 -3.7; 141 -4.2; 155 -4.7; 170 -4.9; 187 -5.3; 206 -5.6; 227 -5.7; 249 -5.7; 274 -5.3; 302 -6.1; 332 -6.1; 365 -5.9; 402 -6.2; 442 -6.4; 486 -6.1; 535 -5.4; 588 -4.8; 647 -4.6; 712 -4.7; 783 -5.1; 861 -6.0; 947 -7.2; 1042 -8.7; 1146 -9.0; 1261 -10.6; 1387 -13.3; 1526 -15.5; 1678 -16.4; 1846 -16.6; 2031 -14.7; 2234 -11.8; 2457 -8.8; 2703 -6.2; 2973 -4.4; 3270 -3.5; 3597 -3.1; 3957 -1.1; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.0; 6373 -7.0; 7010 -11.4; 7711 -10.3; 8482 -9.7; 9330 -11.3; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall Major GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall Major ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.4  | 6.6 dB   |
| Peaking | 717 Hz   | 2.08 | 2.9 dB   |
| Peaking | 1771 Hz  | 1.54 | -13.5 dB |
| Peaking | 5249 Hz  | 0.76 | 15.1 dB  |
| Peaking | 7210 Hz  | 1.14 | -14.9 dB |
| Peaking | 27 Hz    | 0.54 | 1.4 dB   |
| Peaking | 35 Hz    | 1.44 | -2.0 dB  |
| Peaking | 9601 Hz  | 5.83 | -5.3 dB  |
| Peaking | 9907 Hz  | 2.14 | 2.5 dB   |
| Peaking | 20949 Hz | 1.38 | -0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 5.2 dB   |
| Peaking | 125 Hz   | 1.41 | 2.1 dB   |
| Peaking | 250 Hz   | 1.41 | -0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.3 dB |
| Peaking | 4000 Hz  | 1.41 | 10.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Marshall%20Major/Marshall%20Major.png)