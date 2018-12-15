# Sony MDR-ZX110NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.1; 28 1.2; 31 0.4; 34 -0.3; 37 -0.8; 41 -1.5; 45 -2.1; 49 -2.5; 54 -3.1; 60 -3.6; 66 -4.2; 72 -4.6; 79 -4.9; 87 -5.3; 96 -5.5; 106 -5.6; 116 -5.7; 128 -5.6; 141 -5.4; 155 -5.3; 170 -5.0; 187 -4.8; 206 -4.4; 227 -4.1; 249 -3.8; 274 -3.6; 302 -3.3; 332 -2.7; 365 -1.7; 402 -0.3; 442 0.2; 486 -0.1; 535 -0.2; 588 -0.2; 647 -0.2; 712 -0.2; 783 -0.1; 861 0.3; 947 0.3; 1042 -0.5; 1146 -1.8; 1261 -2.3; 1387 -2.7; 1526 -2.4; 1678 -1.7; 1846 -0.5; 2031 0.6; 2234 2.0; 2457 3.3; 2703 3.6; 2973 3.1; 3270 2.9; 3597 3.9; 3957 5.0; 4353 5.6; 4788 6.0; 5267 6.0; 5793 5.8; 6373 2.3; 7010 -1.3; 7711 -3.9; 8482 -6.4; 9330 -6.9; 10263 -2.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.1; 18182 -1.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX110NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX110NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.43 | 4.2 dB  |
| Peaking | 104 Hz   | 0.61 | -5.6 dB |
| Peaking | 233 Hz   | 1.5  | -1.8 dB |
| Peaking | 4962 Hz  | 1.22 | 7.4 dB  |
| Peaking | 8583 Hz  | 2.45 | -9.5 dB |
| Peaking | 1015 Hz  | 0.9  | 2.0 dB  |
| Peaking | 1376 Hz  | 1.44 | -4.7 dB |
| Peaking | 2488 Hz  | 3.55 | 2.7 dB  |
| Peaking | 11324 Hz | 6.33 | 1.7 dB  |
| Peaking | 17446 Hz | 4    | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-ZX110NC/Sony%20MDR-ZX110NC.png)