# Ultrasone Signature Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.2; 23 -0.6; 25 -1.0; 28 -1.6; 31 -2.0; 34 -2.4; 37 -2.7; 41 -3.0; 45 -3.3; 49 -3.5; 54 -3.6; 60 -3.6; 66 -3.6; 72 -2.5; 79 -0.5; 87 -2.8; 96 -5.4; 106 -6.5; 116 -6.0; 128 -6.3; 141 -7.2; 155 -7.0; 170 -5.3; 187 -6.0; 206 -4.9; 227 -3.5; 249 -2.0; 274 -0.8; 302 -0.1; 332 0.0; 365 -0.1; 402 -0.2; 442 -0.6; 486 -1.0; 535 -1.1; 588 -1.1; 647 -1.0; 712 -0.6; 783 -0.7; 861 -0.6; 947 -0.4; 1042 0.3; 1146 1.0; 1261 0.4; 1387 -0.5; 1526 -0.8; 1678 0.2; 1846 2.2; 2031 3.6; 2234 4.8; 2457 6.0; 2703 6.0; 2973 6.0; 3270 5.9; 3597 5.6; 3957 5.6; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.9; 6373 1.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -3.6; 10263 -4.6; 11289 -4.2; 12418 -3.6; 13660 -1.6; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Signature Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Signature Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 1.44 | -3.0 dB |
| Peaking | 141 Hz   | 1.22 | -7.3 dB |
| Peaking | 1444 Hz  | 0.74 | -5.5 dB |
| Peaking | 3027 Hz  | 0.44 | 8.8 dB  |
| Peaking | 10450 Hz | 1.51 | -7.2 dB |
| Peaking | 167 Hz   | 5.41 | 1.8 dB  |
| Peaking | 193 Hz   | 2.99 | -2.0 dB |
| Peaking | 312 Hz   | 1.82 | 2.1 dB  |
| Peaking | 583 Hz   | 0.53 | -0.8 dB |
| Peaking | 1117 Hz  | 4.58 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20Signature%20Pro/Ultrasone%20Signature%20Pro.png)