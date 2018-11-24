# Ultrasone Zino

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.5; 31 4.4; 34 3.2; 37 2.2; 41 1.2; 45 0.4; 49 -0.2; 54 -0.8; 60 -1.2; 66 -1.3; 72 -1.5; 79 -1.6; 87 -1.7; 96 -1.5; 106 -1.3; 116 -1.2; 128 -0.9; 141 -0.7; 155 -0.4; 170 0.0; 187 0.5; 206 1.2; 227 1.9; 249 1.3; 274 1.6; 302 2.1; 332 2.9; 365 3.7; 402 4.3; 442 5.0; 486 5.8; 535 6.0; 588 6.0; 647 6.0; 712 6.0; 783 6.0; 861 5.7; 947 2.1; 1042 -1.5; 1146 -4.1; 1261 -6.8; 1387 -8.5; 1526 -9.6; 1678 -11.6; 1846 -13.4; 2031 -14.5; 2234 -12.8; 2457 -5.4; 2703 -5.9; 2973 -5.1; 3270 -4.0; 3597 -3.2; 3957 0.2; 4353 -4.8; 4788 -1.7; 5267 -0.8; 5793 -4.4; 6373 -4.5; 7010 -0.3; 7711 -2.2; 8482 -7.0; 9330 -11.0; 10263 -9.5; 11289 -3.9; 12418 -0.1; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Zino GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Zino ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 25 Hz    |  2.38 | 7.4 dB   |
| Peaking | 661 Hz   |  0.99 | 9.0 dB   |
| Peaking | 1802 Hz  |  1.3  | -15.5 dB |
| Peaking | 9563 Hz  |  3.6  | -12.0 dB |
| Peaking | 20129 Hz |  3.86 | -3.5 dB  |
| Peaking | 87 Hz    |  1.09 | -2.1 dB  |
| Peaking | 657 Hz   |  2.28 | -5.6 dB  |
| Peaking | 767 Hz   |  1.1  | 5.5 dB   |
| Peaking | 1148 Hz  |  2.54 | -4.2 dB  |
| Peaking | 3862 Hz  | 13.99 | 3.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20Zino/Ultrasone%20Zino.png)