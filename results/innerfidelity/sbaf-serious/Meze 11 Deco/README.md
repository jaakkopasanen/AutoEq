# Meze 11 Deco
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.2; 23 -18.2; 25 -18.2; 28 -18.3; 31 -18.3; 34 -18.4; 37 -18.4; 41 -18.4; 45 -18.4; 49 -18.5; 54 -18.5; 60 -18.6; 66 -18.7; 72 -18.9; 79 -19.0; 87 -19.1; 96 -19.2; 106 -19.2; 116 -19.0; 128 -18.9; 141 -18.8; 155 -18.5; 170 -18.2; 187 -17.8; 206 -17.3; 227 -16.7; 249 -16.2; 274 -15.6; 302 -14.9; 332 -14.3; 365 -13.5; 402 -12.9; 442 -11.9; 486 -11.4; 535 -10.6; 588 -9.8; 647 -8.5; 712 -8.2; 783 -6.9; 861 -6.7; 947 -6.7; 1042 -6.4; 1146 -6.2; 1261 -6.1; 1387 -6.3; 1526 -7.0; 1678 -9.0; 1846 -10.8; 2031 -10.4; 2234 -8.9; 2457 -6.5; 2703 -4.3; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -2.2; 5267 -3.0; 5793 -6.1; 6373 -13.6; 7010 -10.9; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 11 Deco GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 11 Deco ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.19 | -10.7 dB |
| Peaking | 178 Hz   | 0.4  | -9.1 dB  |
| Peaking | 2055 Hz  | 1.7  | -13.1 dB |
| Peaking | 2754 Hz  | 0.56 | 10.4 dB  |
| Peaking | 6538 Hz  | 4.54 | -11.8 dB |
| Peaking | 804 Hz   | 9.22 | 1.0 dB   |
| Peaking | 1757 Hz  | 9.14 | -1.3 dB  |
| Peaking | 2623 Hz  | 7.41 | -1.4 dB  |
| Peaking | 5633 Hz  | 0.5  | 0.8 dB   |
| Peaking | 10047 Hz | 1.03 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.0 dB |
| Peaking | 62 Hz    | 1.41 | -8.5 dB  |
| Peaking | 125 Hz   | 1.41 | -10.2 dB |
| Peaking | 250 Hz   | 1.41 | -7.8 dB  |
| Peaking | 500 Hz   | 1.41 | -3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 16000 Hz | 1.41 | 0.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2011%20Deco/Meze%2011%20Deco.png)