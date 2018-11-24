# Sony MDR-XB80BS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.0; 23 -2.1; 25 -2.1; 28 -2.1; 31 -2.2; 34 -2.3; 37 -2.4; 41 -2.5; 45 -2.7; 49 -2.9; 54 -3.1; 60 -3.4; 66 -3.7; 72 -4.0; 79 -4.3; 87 -4.7; 96 -5.4; 106 -5.7; 116 -5.8; 128 -5.8; 141 -5.6; 155 -5.3; 170 -4.7; 187 -4.0; 206 -3.2; 227 -2.3; 249 -1.6; 274 -1.0; 302 -0.5; 332 -0.1; 365 0.1; 402 0.1; 442 0.0; 486 -0.0; 535 -0.1; 588 -0.1; 647 -0.1; 712 0.0; 783 0.1; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.0; 1261 0.3; 1387 1.0; 1526 1.8; 1678 2.4; 1846 2.9; 2031 3.1; 2234 3.1; 2457 2.8; 2703 3.0; 2973 4.3; 3270 5.9; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 4.4; 5793 0.7; 6373 2.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.1; 15026 -5.1; 16529 -9.9; 18182 -10.4; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB80BS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB80BS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 47 Hz    | 0.46 | -2.3 dB  |
| Peaking | 128 Hz   | 1.12 | -5.1 dB  |
| Peaking | 1862 Hz  | 3    | 1.9 dB   |
| Peaking | 3979 Hz  | 1.2  | 6.5 dB   |
| Peaking | 18176 Hz | 1.25 | -12.0 dB |
| Peaking | 191 Hz   | 4.25 | -0.7 dB  |
| Peaking | 348 Hz   | 2.17 | 0.9 dB   |
| Peaking | 13429 Hz | 2.67 | 3.1 dB   |
| Peaking | 15789 Hz | 3.77 | -3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20MDR-XB80BS/Sony%20MDR-XB80BS.png)