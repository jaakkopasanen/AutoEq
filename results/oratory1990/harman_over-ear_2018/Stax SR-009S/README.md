# Stax SR-009S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.6; 96 -0.8; 106 -1.2; 116 -1.3; 128 -1.6; 141 -1.9; 155 -2.1; 170 -2.5; 187 -2.6; 206 -2.7; 227 -2.8; 249 -2.8; 274 -2.8; 302 -2.8; 332 -2.8; 365 -2.8; 402 -3.0; 442 -3.2; 486 -3.5; 535 -3.7; 588 -4.0; 647 -4.4; 712 -4.8; 783 -4.6; 861 -5.5; 947 -6.2; 1042 -6.4; 1146 -5.8; 1261 -5.9; 1387 -5.8; 1526 -5.4; 1678 -4.2; 1846 -2.8; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -1.2; 3270 -1.1; 3597 -2.1; 3957 -3.1; 4353 -3.6; 4788 -5.3; 5267 -4.2; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-009S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-65**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.2  | 6.2 dB  |
| Peaking | 408 Hz   | 1.25 | 2.2 dB  |
| Peaking | 2631 Hz  | 1.42 | 6.5 dB  |
| Peaking | 6094 Hz  | 4.82 | 5.8 dB  |
| Peaking | 20054 Hz | 2.14 | -6.3 dB |
| Peaking | 1331 Hz  | 1.92 | -1.0 dB |
| Peaking | 2050 Hz  | 4.68 | 2.2 dB  |
| Peaking | 2947 Hz  | 1.66 | -1.5 dB |
| Peaking | 3445 Hz  | 3.43 | 2.1 dB  |
| Peaking | 8311 Hz  | 4.58 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Stax%20SR-009S/Stax%20SR-009S.png)