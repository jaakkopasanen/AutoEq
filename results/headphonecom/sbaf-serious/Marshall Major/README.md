# Marshall Major
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.7; 116 -1.3; 128 -2.0; 141 -2.4; 155 -3.0; 170 -3.2; 187 -3.5; 206 -3.8; 227 -4.0; 249 -3.9; 274 -3.6; 302 -4.3; 332 -4.4; 365 -4.2; 402 -4.4; 442 -4.6; 486 -4.3; 535 -3.6; 588 -3.0; 647 -2.8; 712 -2.9; 783 -3.4; 861 -4.2; 947 -5.5; 1042 -6.9; 1146 -7.2; 1261 -8.8; 1387 -11.5; 1526 -13.7; 1678 -14.7; 1846 -14.9; 2031 -12.9; 2234 -10.1; 2457 -7.0; 2703 -4.4; 2973 -2.6; 3270 -1.7; 3597 -1.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.4; 6373 -5.3; 7010 -9.7; 7711 -8.6; 8482 -7.9; 9330 -9.5; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall Major GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall Major ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.15 | 6.0 dB   |
| Peaking | 94 Hz   | 2.01 | 1.2 dB   |
| Peaking | 699 Hz  | 1.38 | 3.9 dB   |
| Peaking | 1741 Hz | 1.93 | -10.6 dB |
| Peaking | 3872 Hz | 1.45 | 7.7 dB   |
| Peaking | 2137 Hz | 5.94 | -1.2 dB  |
| Peaking | 2940 Hz | 2.44 | 2.1 dB   |
| Peaking | 3636 Hz | 2.86 | -2.0 dB  |
| Peaking | 5676 Hz | 2.51 | 7.5 dB   |
| Peaking | 6888 Hz | 1.61 | -6.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | 3.9 dB  |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.4 dB |
| Peaking | 4000 Hz  | 1.41 | 10.5 dB |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Marshall%20Major/Marshall%20Major.png)