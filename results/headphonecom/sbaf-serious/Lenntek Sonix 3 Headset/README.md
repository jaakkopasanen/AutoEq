# Lenntek Sonix 3 Headset

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.7; 54 5.5; 60 5.2; 66 4.9; 72 4.4; 79 4.1; 87 3.8; 96 3.5; 106 3.2; 116 2.8; 128 2.5; 141 2.2; 155 2.0; 170 1.8; 187 1.7; 206 1.4; 227 1.3; 249 1.3; 274 1.3; 302 1.4; 332 1.3; 365 1.5; 402 1.5; 442 1.4; 486 1.5; 535 1.5; 588 1.5; 647 1.5; 712 1.5; 783 1.2; 861 0.9; 947 0.3; 1042 -0.3; 1146 -0.8; 1261 -1.3; 1387 -2.1; 1526 -3.4; 1678 -4.8; 1846 -6.0; 2031 -6.8; 2234 -6.4; 2457 -4.0; 2703 -0.8; 2973 1.9; 3270 3.3; 3597 3.5; 3957 0.2; 4353 -5.0; 4788 -2.0; 5267 4.2; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -1.3; 8482 -2.6; 9330 -0.4; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lenntek Sonix 3 Headset GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lenntek Sonix 3 Headset ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.12 | 6.1 dB  |
| Peaking | 2062 Hz | 2.11 | -8.2 dB |
| Peaking | 3393 Hz | 2.46 | 5.9 dB  |
| Peaking | 4439 Hz | 5.29 | -8.3 dB |
| Peaking | 5794 Hz | 3.9  | 7.5 dB  |
| Peaking | 148 Hz  | 1.25 | -0.6 dB |
| Peaking | 606 Hz  | 0.91 | 1.6 dB  |
| Peaking | 1528 Hz | 3.26 | -1.0 dB |
| Peaking | 6697 Hz | 7.22 | 2.2 dB  |
| Peaking | 8209 Hz | 5.11 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Lenntek%20Sonix%203%20Headset/Lenntek%20Sonix%203%20Headset.png)