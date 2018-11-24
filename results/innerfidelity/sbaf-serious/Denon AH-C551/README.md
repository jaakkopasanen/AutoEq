# Denon AH-C551

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 21 -5.7; 23 -6.1; 25 -6.4; 28 -6.8; 31 -7.0; 34 -7.3; 37 -7.5; 41 -7.8; 45 -8.0; 49 -8.2; 54 -8.3; 60 -8.6; 66 -8.8; 72 -9.0; 79 -9.3; 87 -9.5; 96 -9.7; 106 -9.7; 116 -9.6; 128 -9.6; 141 -9.5; 155 -9.3; 170 -9.0; 187 -8.6; 206 -8.2; 227 -7.6; 249 -7.1; 274 -6.5; 302 -5.8; 332 -5.1; 365 -4.3; 402 -3.6; 442 -2.8; 486 -2.1; 535 -1.4; 588 -0.5; 647 -0.0; 712 0.3; 783 0.8; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -2.0; 1526 -3.1; 1678 -4.0; 1846 -4.7; 2031 -5.3; 2234 -6.3; 2457 -7.7; 2703 -9.4; 2973 -9.7; 3270 -6.4; 3597 -4.0; 3957 -3.9; 4353 -6.1; 4788 -8.1; 5267 -10.2; 5793 -10.9; 6373 -7.4; 7010 -4.8; 7711 -4.2; 8482 -6.3; 9330 -7.1; 10263 -2.5; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.5; 16529 -2.0; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C551 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-8**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C551 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 55 Hz    | 0.33 | -7.9 dB |
| Peaking | 181 Hz   | 0.78 | -5.1 dB |
| Peaking | 2602 Hz  | 1.98 | -8.1 dB |
| Peaking | 5762 Hz  | 1.5  | -9.3 dB |
| Peaking | 15998 Hz | 3.66 | -2.1 dB |
| Peaking | 775 Hz   | 2.77 | 2.2 dB  |
| Peaking | 5606 Hz  | 3.99 | -3.9 dB |
| Peaking | 6757 Hz  | 1.47 | 4.1 dB  |
| Peaking | 9250 Hz  | 2.87 | -8.3 dB |
| Peaking | 10784 Hz | 2.31 | 3.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C551/Denon%20AH-C551.png)