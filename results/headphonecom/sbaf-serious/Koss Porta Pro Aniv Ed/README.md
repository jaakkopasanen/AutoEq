# Koss Porta Pro Aniv Ed

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 5.0; 34 4.0; 37 3.1; 41 2.1; 45 1.1; 49 0.3; 54 -0.8; 60 -1.8; 66 -2.7; 72 -3.5; 79 -4.3; 87 -4.9; 96 -5.5; 106 -5.9; 116 -5.9; 128 -6.0; 141 -5.9; 155 -6.0; 170 -5.7; 187 -5.5; 206 -5.0; 227 -4.5; 249 -3.9; 274 -3.5; 302 -3.0; 332 -2.5; 365 -2.1; 402 -1.7; 442 -1.4; 486 -0.8; 535 -0.6; 588 -0.3; 647 0.1; 712 0.0; 783 0.2; 861 0.1; 947 -0.0; 1042 -0.1; 1146 -0.3; 1261 -0.7; 1387 -1.4; 1526 -2.5; 1678 -3.3; 1846 -4.2; 2031 -4.6; 2234 -4.3; 2457 -2.5; 2703 -0.2; 2973 2.6; 3270 4.2; 3597 4.9; 3957 1.6; 4353 0.7; 4788 -0.1; 5267 2.5; 5793 5.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.2; 9330 -2.2; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.3; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro Aniv Ed GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro Aniv Ed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.71 | 7.3 dB  |
| Peaking | 121 Hz   | 0.48 | -6.9 dB |
| Peaking | 2036 Hz  | 1.13 | -9.7 dB |
| Peaking | 2312 Hz  | 0.41 | 4.9 dB  |
| Peaking | 3268 Hz  | 3.87 | 4.6 dB  |
| Peaking | 4757 Hz  | 4.27 | -3.1 dB |
| Peaking | 6064 Hz  | 3.62 | 5.3 dB  |
| Peaking | 8903 Hz  | 3.65 | -3.7 dB |
| Peaking | 20231 Hz | 4.79 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20Porta%20Pro%20Aniv%20Ed/Koss%20Porta%20Pro%20Aniv%20Ed.png)