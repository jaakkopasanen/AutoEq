# Beyerdynamic T90 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.9; 25 -3.1; 28 -3.3; 31 -3.6; 34 -3.7; 37 -3.9; 41 -3.9; 45 -3.9; 49 -3.9; 54 -3.8; 60 -3.0; 66 -4.4; 72 -5.4; 79 -6.0; 87 -6.3; 96 -6.7; 106 -7.1; 116 -7.4; 128 -7.8; 141 -8.2; 155 -8.4; 170 -8.3; 187 -8.6; 206 -8.6; 227 -8.6; 249 -8.5; 274 -8.4; 302 -8.2; 332 -7.8; 365 -7.5; 402 -6.9; 442 -6.7; 486 -6.3; 535 -5.6; 588 -4.8; 647 -4.6; 712 -3.8; 783 -3.5; 861 -3.1; 947 -3.4; 1042 -3.7; 1146 -3.9; 1261 -4.2; 1387 -5.2; 1526 -5.9; 1678 -6.4; 1846 -7.2; 2031 -7.4; 2234 -7.0; 2457 -7.1; 2703 -7.6; 2973 -8.4; 3270 -8.8; 3597 -8.2; 3957 -8.1; 4353 -7.8; 4788 -0.5; 5267 -2.1; 5793 -4.8; 6373 -11.8; 7010 -12.4; 7711 -13.9; 8482 -15.1; 9330 -14.9; 10263 -13.0; 11289 -11.9; 12418 -11.6; 13660 -8.7; 15026 -6.7; 16529 -10.4; 18182 -13.2; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T90 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T90 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 201 Hz   | 0.65 | -5.3 dB  |
| Peaking | 1979 Hz  | 2.63 | -3.2 dB  |
| Peaking | 3188 Hz  | 3.44 | -4.3 dB  |
| Peaking | 9052 Hz  | 1.4  | -11.8 dB |
| Peaking | 17974 Hz | 1.12 | -9.3 dB  |
| Peaking | 876 Hz   | 1.77 | 2.0 dB   |
| Peaking | 2213 Hz  | 0.15 | -0.7 dB  |
| Peaking | 4297 Hz  | 4.08 | -7.6 dB  |
| Peaking | 4899 Hz  | 2.56 | 10.4 dB  |
| Peaking | 6588 Hz  | 5.26 | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB   |
| Peaking | 62 Hz    | 1.41 | 0.1 dB   |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -11.1 dB |
| Peaking | 16000 Hz | 1.41 | -7.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T90%20250%20Ohm/Beyerdynamic%20T90%20250%20Ohm.png)