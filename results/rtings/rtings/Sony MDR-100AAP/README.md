# Sony MDR-100AAP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 -1.9; 23 -2.4; 25 -2.8; 28 -3.4; 31 -3.9; 34 -4.3; 37 -4.5; 41 -4.7; 45 -4.8; 49 -4.8; 54 -4.9; 60 -5.0; 66 -5.0; 72 -5.0; 79 -5.2; 87 -5.6; 96 -6.0; 106 -6.3; 116 -6.5; 128 -6.5; 141 -6.3; 155 -6.1; 170 -5.9; 187 -5.4; 206 -4.6; 227 -3.4; 249 -3.3; 274 -4.4; 302 -3.3; 332 -2.1; 365 -1.2; 402 -0.7; 442 -0.6; 486 -0.6; 535 -0.6; 588 -0.6; 647 -0.6; 712 -0.4; 783 -0.3; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.1; 1261 0.0; 1387 -0.0; 1526 -0.1; 1678 -0.2; 1846 -0.0; 2031 0.1; 2234 0.9; 2457 1.8; 2703 2.7; 2973 3.3; 3270 2.5; 3597 2.0; 3957 1.7; 4353 1.7; 4788 3.7; 5267 0.2; 5793 2.1; 6373 1.6; 7010 1.9; 7711 0.3; 8482 -1.1; 9330 -1.7; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-100AAP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-100AAP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.57 | -4.0 dB |
| Peaking | 140 Hz  | 0.91 | -5.4 dB |
| Peaking | 282 Hz  | 5.36 | -2.0 dB |
| Peaking | 2907 Hz | 3.37 | 3.0 dB  |
| Peaking | 4735 Hz | 2.05 | 2.2 dB  |
| Peaking | 190 Hz  | 8.56 | -0.6 dB |
| Peaking | 403 Hz  | 5.06 | 0.5 dB  |
| Peaking | 1759 Hz | 4.25 | -0.5 dB |
| Peaking | 6852 Hz | 4.85 | 1.3 dB  |
| Peaking | 8933 Hz | 6.65 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20MDR-100AAP/Sony%20MDR-100AAP.png)