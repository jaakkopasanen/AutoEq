# Altec Lansing True Evo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.5dB
GraphicEQ: 21 -0.9; 23 -1.1; 25 -1.2; 28 -1.6; 31 -1.9; 34 -2.3; 37 -2.7; 41 -3.3; 45 -3.9; 49 -4.6; 54 -5.6; 60 -6.9; 66 -8.3; 72 -9.5; 79 -10.8; 87 -12.2; 96 -13.4; 106 -14.3; 116 -14.8; 128 -14.8; 141 -14.6; 155 -14.2; 170 -13.8; 187 -13.2; 206 -12.6; 227 -11.7; 249 -10.7; 274 -9.7; 302 -8.7; 332 -7.7; 365 -6.8; 402 -5.9; 442 -4.9; 486 -4.1; 535 -3.2; 588 -2.5; 647 -1.8; 712 -1.1; 783 -0.6; 861 -0.5; 947 -1.0; 1042 -1.8; 1146 -2.0; 1261 -2.5; 1387 -2.7; 1526 -2.8; 1678 -2.9; 1846 -3.0; 2031 -3.1; 2234 -2.7; 2457 -2.3; 2703 -3.0; 2973 -4.4; 3270 -5.6; 3597 -5.9; 3957 -5.7; 4353 -5.7; 4788 -5.3; 5267 -5.8; 5793 -7.6; 6373 -11.1; 7010 -10.6; 7711 -6.9; 8482 -4.8; 9330 -5.5; 10263 -5.5; 11289 -2.7; 12418 -1.5; 13660 -2.8; 15026 -6.4; 16529 -7.1; 18182 -6.3; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Altec Lansing True Evo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-14**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Altec Lansing True Evo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 110 Hz   | 0.95 | -11.0 dB |
| Peaking | 212 Hz   | 0.98 | -7.2 dB  |
| Peaking | 1762 Hz  | 3.52 | -1.1 dB  |
| Peaking | 3481 Hz  | 3.02 | -3.3 dB  |
| Peaking | 6715 Hz  | 1.63 | -8.8 dB  |
| Peaking | 24 Hz    | 1.52 | 1.2 dB   |
| Peaking | 374 Hz   | 3.05 | -0.9 dB  |
| Peaking | 780 Hz   | 2.75 | 2.1 dB   |
| Peaking | 8134 Hz  | 6.86 | 2.4 dB   |
| Peaking | 18787 Hz | 0.57 | -6.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Altec%20Lansing%20True%20Evo/Altec%20Lansing%20True%20Evo.png)