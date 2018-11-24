# Denon AH-D2000 B2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 0.0; 23 1.1; 25 0.5; 28 -0.1; 31 -0.5; 34 -0.6; 37 -0.7; 41 -0.8; 45 -0.7; 49 -0.5; 54 -0.4; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.8; 87 -1.1; 96 -1.5; 106 -1.6; 116 -1.8; 128 -2.0; 141 -2.3; 155 -2.2; 170 -2.1; 187 -2.2; 206 -2.3; 227 -2.1; 249 -1.9; 274 -1.8; 302 -1.7; 332 -1.6; 365 -1.3; 402 -1.0; 442 -0.8; 486 -1.0; 535 -1.3; 588 -1.2; 647 -1.3; 712 1.1; 783 0.7; 861 -0.2; 947 -0.2; 1042 0.1; 1146 0.5; 1261 1.0; 1387 1.1; 1526 0.8; 1678 0.7; 1846 1.0; 2031 1.4; 2234 1.5; 2457 1.7; 2703 2.0; 2973 5.2; 3270 4.2; 3597 1.7; 3957 1.2; 4353 1.7; 4788 3.2; 5267 2.7; 5793 2.3; 6373 1.2; 7010 0.4; 7711 0.2; 8482 0.0; 9330 0.0; 10263 -1.5; 11289 -0.5; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D2000 B2012 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 191 Hz   | 0.54 | -2.3 dB |
| Peaking | 1768 Hz  | 0.88 | 1.0 dB  |
| Peaking | 3060 Hz  | 5.58 | 5.0 dB  |
| Peaking | 5192 Hz  | 3.03 | 2.9 dB  |
| Peaking | 10494 Hz | 4.99 | -1.6 dB |
| Peaking | 70 Hz    | 3.69 | 0.4 dB  |
| Peaking | 654 Hz   | 4.21 | -1.9 dB |
| Peaking | 724 Hz   | 5.69 | 2.8 dB  |
| Peaking | 901 Hz   | 5.5  | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D2000%20B2012/Denon%20AH-D2000%20B2012.png)