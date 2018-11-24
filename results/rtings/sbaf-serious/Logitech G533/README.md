# Logitech G533

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 -3.1; 23 -3.4; 25 -3.7; 28 -4.0; 31 -4.3; 34 -4.4; 37 -4.5; 41 -4.4; 45 -4.3; 49 -4.3; 54 -4.3; 60 -4.2; 66 -4.1; 72 -4.0; 79 -3.9; 87 -3.9; 96 -4.1; 106 -4.2; 116 -4.3; 128 -4.3; 141 -4.2; 155 -4.1; 170 -4.0; 187 -3.9; 206 -3.7; 227 -3.5; 249 -3.4; 274 -3.6; 302 -3.8; 332 -3.8; 365 -3.1; 402 -2.3; 442 -1.7; 486 -1.2; 535 -0.5; 588 -0.1; 647 0.2; 712 0.5; 783 1.2; 861 1.3; 947 0.3; 1042 -0.2; 1146 -0.3; 1261 0.1; 1387 1.0; 1526 1.9; 1678 1.3; 1846 0.6; 2031 0.3; 2234 0.4; 2457 1.0; 2703 -1.7; 2973 -0.7; 3270 0.9; 3597 0.4; 3957 -1.4; 4353 -3.2; 4788 -0.9; 5267 2.3; 5793 2.7; 6373 0.6; 7010 0.4; 7711 -0.9; 8482 -5.6; 9330 -6.2; 10263 -0.3; 11289 0.0; 12418 0.0; 13660 -0.4; 15026 -0.0; 16529 0.0; 18182 -2.4; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G533 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G533 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.41 | -4.2 dB |
| Peaking | 156 Hz   | 1.01 | -2.8 dB |
| Peaking | 322 Hz   | 2.43 | -2.9 dB |
| Peaking | 8944 Hz  | 6.35 | -7.9 dB |
| Peaking | 802 Hz   | 4.48 | 1.7 dB  |
| Peaking | 1568 Hz  | 5.01 | 2.1 dB  |
| Peaking | 4416 Hz  | 6    | -4.1 dB |
| Peaking | 5551 Hz  | 4    | 3.6 dB  |
| Peaking | 19694 Hz | 2.5  | -7.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Logitech%20G533/Logitech%20G533.png)