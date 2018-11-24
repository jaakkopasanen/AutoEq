# Logitech G Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 -3.9; 23 -4.3; 25 -4.7; 28 -5.2; 31 -5.5; 34 -5.7; 37 -5.8; 41 -5.8; 45 -5.9; 49 -5.9; 54 -5.9; 60 -5.9; 66 -6.1; 72 -6.2; 79 -6.4; 87 -6.7; 96 -7.2; 106 -8.0; 116 -8.7; 128 -9.2; 141 -9.3; 155 -9.3; 170 -9.2; 187 -8.7; 206 -8.0; 227 -7.1; 249 -5.9; 274 -4.4; 302 -2.9; 332 -1.7; 365 -1.4; 402 -1.7; 442 -2.5; 486 -3.4; 535 -3.9; 588 -4.0; 647 -3.7; 712 -2.8; 783 -1.7; 861 -0.8; 947 -0.2; 1042 -0.0; 1146 -0.3; 1261 -0.9; 1387 -2.3; 1526 -3.2; 1678 -3.3; 1846 -3.0; 2031 -3.0; 2234 -2.6; 2457 -2.8; 2703 -2.4; 2973 -0.5; 3270 0.3; 3597 -2.8; 3957 -3.3; 4353 -3.0; 4788 -2.6; 5267 2.7; 5793 2.3; 6373 1.2; 7010 -2.4; 7711 -5.0; 8482 -8.0; 9330 -9.6; 10263 -6.9; 11289 -1.8; 12418 0.0; 13660 -0.6; 15026 -2.4; 16529 -1.6; 18182 -1.3; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.34 | -5.2 dB  |
| Peaking | 160 Hz   | 1.05 | -7.6 dB  |
| Peaking | 605 Hz   | 2.31 | -3.4 dB  |
| Peaking | 9188 Hz  | 3.03 | -10.5 dB |
| Peaking | 1099 Hz  | 1.63 | 2.3 dB   |
| Peaking | 1670 Hz  | 1.27 | -3.9 dB  |
| Peaking | 4507 Hz  | 2.86 | -4.5 dB  |
| Peaking | 5515 Hz  | 3.65 | 6.1 dB   |
| Peaking | 20851 Hz | 0.98 | -4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Logitech%20G%20Pro/Logitech%20G%20Pro.png)