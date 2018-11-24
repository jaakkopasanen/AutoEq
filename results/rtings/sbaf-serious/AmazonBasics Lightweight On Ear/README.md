# AmazonBasics Lightweight On Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.8; 23 -1.2; 25 -1.5; 28 -2.1; 31 -2.6; 34 -2.9; 37 -3.2; 41 -3.4; 45 -3.6; 49 -3.6; 54 -3.6; 60 -3.5; 66 -3.5; 72 -3.5; 79 -3.4; 87 -3.1; 96 -2.7; 106 -2.1; 116 -1.6; 128 -1.0; 141 -0.5; 155 -0.0; 170 0.7; 187 1.4; 206 2.1; 227 2.8; 249 3.6; 274 4.2; 302 4.4; 332 4.3; 365 3.3; 402 2.2; 442 1.1; 486 -0.1; 535 -1.0; 588 -1.4; 647 -1.4; 712 -1.1; 783 -0.9; 861 -0.6; 947 -0.2; 1042 0.2; 1146 0.8; 1261 1.5; 1387 1.9; 1526 2.1; 1678 2.5; 1846 3.5; 2031 4.4; 2234 5.4; 2457 6.0; 2703 5.9; 2973 5.7; 3270 5.9; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 4.3; 7010 0.3; 7711 0.2; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AmazonBasics Lightweight On Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AmazonBasics Lightweight On Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 1.18 | -2.1 dB |
| Peaking | 76 Hz   | 0.79 | -3.2 dB |
| Peaking | 312 Hz  | 1.03 | 6.0 dB  |
| Peaking | 573 Hz  | 1.02 | -3.8 dB |
| Peaking | 3332 Hz | 0.73 | 6.8 dB  |
| Peaking | 2342 Hz | 4.49 | 1.1 dB  |
| Peaking | 3185 Hz | 3.03 | -1.0 dB |
| Peaking | 5953 Hz | 2.42 | 6.5 dB  |
| Peaking | 6882 Hz | 1.61 | -5.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/AmazonBasics%20Lightweight%20On%20Ear/AmazonBasics%20Lightweight%20On%20Ear.png)