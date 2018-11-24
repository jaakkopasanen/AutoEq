# Sony MDR-1A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -1.7; 23 -2.1; 25 -2.5; 28 -2.9; 31 -3.1; 34 -3.2; 37 -3.2; 41 -3.3; 45 -3.3; 49 -3.3; 54 -3.2; 60 -3.1; 66 -3.1; 72 -3.1; 79 -3.2; 87 -3.4; 96 -3.6; 106 -3.7; 116 -3.7; 128 -3.5; 141 -3.1; 155 -2.4; 170 -1.7; 187 -0.9; 206 -0.3; 227 -0.1; 249 -0.3; 274 0.8; 302 1.9; 332 2.5; 365 2.9; 402 3.0; 442 2.9; 486 2.6; 535 2.2; 588 1.7; 647 1.4; 712 1.1; 783 0.7; 861 0.2; 947 0.0; 1042 0.0; 1146 0.1; 1261 -0.0; 1387 -0.6; 1526 -1.3; 1678 -1.6; 1846 -1.5; 2031 -1.3; 2234 -0.5; 2457 0.9; 2703 2.0; 2973 3.0; 3270 4.0; 3597 5.3; 3957 1.4; 4353 0.5; 4788 4.1; 5267 4.8; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.1; 8482 -5.6; 9330 -7.7; 10263 -1.8; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 233 Hz   | 0.12 | -5.1 dB |
| Peaking | 428 Hz   | 0.57 | 7.8 dB  |
| Peaking | 3281 Hz  | 3.08 | 4.9 dB  |
| Peaking | 5976 Hz  | 2.32 | 6.7 dB  |
| Peaking | 9028 Hz  | 4.58 | -9.8 dB |
| Peaking | 127 Hz   | 4.91 | -0.7 dB |
| Peaking | 1225 Hz  | 4.1  | 1.1 dB  |
| Peaking | 1754 Hz  | 3.85 | -0.9 dB |
| Peaking | 9901 Hz  | 8.42 | -2.3 dB |
| Peaking | 10515 Hz | 4.45 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20MDR-1A/Sony%20MDR-1A.png)