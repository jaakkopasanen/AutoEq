# Audio-Technica ATH-MSR7NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.3; 28 2.8; 31 2.5; 34 2.3; 37 2.2; 41 2.0; 45 1.9; 49 1.8; 54 1.6; 60 1.4; 66 1.1; 72 0.9; 79 0.7; 87 0.3; 96 -0.1; 106 -0.5; 116 -0.8; 128 -1.1; 141 -1.2; 155 -1.3; 170 -1.3; 187 -1.2; 206 -1.1; 227 -0.8; 249 -0.4; 274 0.2; 302 1.7; 332 3.1; 365 4.3; 402 4.3; 442 3.8; 486 3.3; 535 2.9; 588 2.5; 647 2.2; 712 1.9; 783 1.3; 861 0.8; 947 0.3; 1042 -0.0; 1146 -0.2; 1261 -0.7; 1387 -1.6; 1526 -3.2; 1678 -4.3; 1846 -4.7; 2031 -4.9; 2234 -4.2; 2457 -2.6; 2703 -1.4; 2973 -0.2; 3270 1.5; 3597 3.5; 3957 2.8; 4353 -1.5; 4788 -1.4; 5267 1.4; 5793 4.4; 6373 5.3; 7010 2.5; 7711 -0.9; 8482 -2.7; 9330 -2.5; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-MSR7NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-MSR7NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.91 | 3.7 dB  |
| Peaking | 447 Hz  | 1.69 | 4.4 dB  |
| Peaking | 1935 Hz | 1.98 | -5.4 dB |
| Peaking | 3603 Hz | 6.15 | 4.7 dB  |
| Peaking | 6219 Hz | 6.12 | 6.2 dB  |
| Peaking | 183 Hz  | 1.24 | -1.9 dB |
| Peaking | 348 Hz  | 5.21 | 2.0 dB  |
| Peaking | 4572 Hz | 6.62 | -3.9 dB |
| Peaking | 6493 Hz | 0.89 | 1.7 dB  |
| Peaking | 8690 Hz | 3.12 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-MSR7NC/Audio-Technica%20ATH-MSR7NC.png)