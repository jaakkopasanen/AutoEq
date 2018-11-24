# Bowers & Wilkins P5 Test 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 21 -1.6; 23 -1.8; 25 -1.9; 28 -2.1; 31 -2.2; 34 -2.3; 37 -2.4; 41 -2.5; 45 -2.7; 49 -2.9; 54 -3.2; 60 -3.5; 66 -3.9; 72 -4.2; 79 -4.4; 87 -4.9; 96 -5.2; 106 -5.5; 116 -5.7; 128 -5.9; 141 -6.1; 155 -6.4; 170 -6.1; 187 -6.1; 206 -5.7; 227 -5.1; 249 -4.4; 274 -3.5; 302 -3.5; 332 -3.4; 365 -2.5; 402 -1.6; 442 -0.7; 486 -0.5; 535 -0.3; 588 0.1; 647 -0.1; 712 -0.2; 783 0.0; 861 -0.1; 947 -0.0; 1042 0.0; 1146 -0.0; 1261 -0.2; 1387 -0.7; 1526 -1.4; 1678 -2.0; 1846 -2.5; 2031 -2.7; 2234 -3.6; 2457 -3.9; 2703 -3.3; 2973 -2.8; 3270 -1.8; 3597 -1.0; 3957 0.3; 4353 0.4; 4788 0.4; 5267 -0.6; 5793 -2.3; 6373 0.6; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.4; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Test 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Test 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.46 | -1.3 dB |
| Peaking | 102 Hz  | 0.63 | -2.9 dB |
| Peaking | 195 Hz  | 0.71 | -4.8 dB |
| Peaking | 1122 Hz | 0.16 | 1.3 dB  |
| Peaking | 2340 Hz | 1.27 | -5.0 dB |
| Peaking | 344 Hz  | 3.84 | -1.9 dB |
| Peaking | 356 Hz  | 1.87 | 1.2 dB  |
| Peaking | 4824 Hz | 2.44 | 2.8 dB  |
| Peaking | 5874 Hz | 2.2  | -4.9 dB |
| Peaking | 6758 Hz | 5.42 | 5.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P5%20Test%202/Bowers%20&%20Wilkins%20P5%20Test%202.png)